from pytorch_lightning.loggers import WandbLogger

def logger_preference(project_name,classes,dataset_size,useModel,cutlen,minepoch,target):
    return WandbLogger(
        project=project_name,
        config={
            "dataset_size" : dataset_size,
            "model" : useModel,
            "cutlen" : cutlen,
            "target" : target,
        },
        name=useModel+"_"+str(classes)+"_"+str(cutlen)+"_e_"+str(minepoch)+"_"+str(target)
    )