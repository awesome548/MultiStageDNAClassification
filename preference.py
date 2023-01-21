from models import LSTM,resnet,SimpleViT,ViT,ViT2,SimpleViT2,Transformer_clf_model,GRU,effnetv2_s,gru
from pytorch_lightning.loggers import WandbLogger

DEFAULT_CNN = {
    "channel" : 20,
    "kernel" : 19,
    "stride" : 3,
    "padd" : 5,
}
def model_parameter(flag,hidden):
    if flag == 0:
        ##LSTM
        model_params = {
            'hiddenDim' : hidden,
            'bidirect' : True,
        }
    elif flag == 1:
        ##transformer
        model_params = {
            'heads' : 8,
            'depth' : 4,
        }
    elif flag == 2:
        ##cosformer
        model_params = {
            #'use_cos': False,
            #'kernel': 'elu',
            'use_cos': True,
            'kernel': 'relu',
            'd_model': 112,
            'n_heads': 8,
            'n_layers': 3,
            'ffn_ratio': 8,
            'rezero': False,
            'ln_eps': 1e-5,
            'denom_eps': 1e-5,
            'bias': False,
            'dropout': 0.2,    
            'xavier': True,
        }

    return model_params

def data_preference(cutoff,cutlen):
    dataset_size = 10000
    
    cut_size = {
        'cutoff' : cutoff,
        'cutlen' : cutlen,
        'maxlen' : 10000,
        'stride' : 5000 if cutlen<=5000 else (10000-cutlen),
    }
    return dataset_size,cut_size

def model_preference(arch,hidden,classes,cutlen,learningrate,target,epoch,heatmap,project,mode=0,cnn_params=None,cfgs=None):
    """
    cnn_params = {
        "channel" : 112,
        "kernel" : 23,
        "stride" : 2,
        "padd" : 3,
    }
    optim logs
    EFFNET : 112, 23, 2, 3
    GRU : 'out_dim': 91, 'kernel': 14, 'stride': 2
    TRANS : out_dim': 112.0, 'kernel': 17, 'stride': 5, 'n_layers': 3, 'ffn_ratio': 8
    """
    pref = {
        "lr" : learningrate,
        "cutlen" : cutlen,
        "classes" : classes,
        "epoch" : epoch,
        "target" : target,
        "name" : arch,
        "heatmap" : heatmap,
        "project" : project,
    }
    if "GRU" in str(arch):
        params = model_parameter(0,hidden)
        model = gru(param=params,preference=pref)
    elif "ResNet" in str(arch):
        model = resnet(mode=mode,preference=pref,cnnparam=DEFAULT_CNN)
        #model = resnet(preference=pref,mode=mode)
    elif "Transformer" in str(arch):
        params = model_parameter(2,hidden)
        model = Transformer_clf_model(cnn_params,model_type='kernel', model_args=params,preference=pref)
    elif "LSTM" in str(arch):
        params = model_parameter(0,hidden)
        model = LSTM(**params,**pref)
    elif "Effnet" in str(arch):
        model = effnetv2_s(mode=mode,preference=pref)
    else:
        raise NotImplementedError("model selection error")
    useModel = arch
    return model,useModel

def logger_preference(project_name,classes,dataset_size,useModel,cutlen,minepoch,target):
    return WandbLogger(
        project=project_name,
        config={
            "dataset_size" : dataset_size,
            "model" : useModel,
            "cutlen" : cutlen,
            "target" : target,
            "epoch" : minepoch
        },
        name=useModel+"_"+str(classes)+"_"+str(cutlen)+"_e_"+str(minepoch)+"_"+str(target)
    )
