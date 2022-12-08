import torch

def double_data(a:torch.Tensor,b:torch.Tensor,isFormat:bool,dim:int,length:int):
      if isFormat:
            return (torch.cat((a,b))).view(-1,dim,length)
      else:
            return torch.cat((a,b))

def double_labels(a:torch.Tensor,b:torch.Tensor):
      a_labels = torch.zeros(a.shape[0])
      b_labels = torch.ones(b.shape[0])
      return (torch.cat((a_labels,b_labels),dim=0).clone().detach()).to(torch.int64)

def triple_data(a:torch.Tensor,b:torch.Tensor,c:torch.Tensor,isFormat:bool,dim:int,length:int):
      if isFormat:
            return (torch.cat((a,b,c))).view(-1,dim,length)
      else:
            return torch.cat((a,b,c))

def triple_labels(a:torch.Tensor,b:torch.Tensor,c:torch.Tensor):
      #a_labels = torch.zeros(a.shape[0])
      a_labels = torch.ones(a.shape[0])*2
      b_labels = torch.ones(b.shape[0])
      #c_labels = torch.ones(c.shape[0])*2
      c_labels = torch.zeros(c.shape[0])
      return (torch.cat((a_labels,b_labels,c_labels),dim=0).clone().detach()).to(torch.int64)

def quad_data(a:torch.Tensor,b:torch.Tensor,c:torch.Tensor,d:torch.Tensor,isFormat:bool,dim:int,length:int):
      if isFormat:
            return (torch.cat((a,b,c,d))).view(-1,dim,length)
      else:
            return torch.cat((a,b,c,d))

def quad_labels(a:torch.Tensor,b:torch.Tensor,c:torch.Tensor,d:torch.Tensor):
      #a_labels = torch.zeros(a.shape[0])
      a_labels = torch.ones(a.shape[0])*2
      b_labels = torch.ones(b.shape[0])
      #c_labels = torch.ones(c.shape[0])*2
      c_labels = torch.zeros(c.shape[0])
      d_labels = torch.ones(d.shape[0])*3
      return (torch.cat((a_labels,b_labels,c_labels,d_labels),dim=0).clone().detach()).to(torch.int64)

def base_data(a,b,c,d,e,f,isFormat:bool,dim:int,length:int):
      if isFormat:
            return (torch.cat((a,b,c,d,e,f))).view(-1,dim,length)
      else:
            return torch.cat((a,b,c,d,e,f))

def base_labels(a,b,c,d,e,f):
      #a_labels = torch.zeros(a.shape[0])
      f_labels = torch.zeros(f.shape[0])
      b_labels = torch.ones(b.shape[0])
      c_labels = torch.ones(c.shape[0])*2
      d_labels = torch.ones(d.shape[0])*3
      e_labels = torch.ones(e.shape[0])*4
      #f_labels = torch.ones(f.shape[0])*5
      a_labels = torch.ones(a.shape[0])*5
      return (torch.cat((a_labels,b_labels,c_labels,d_labels),dim=0).clone().detach()).to(torch.int64)

class MultiDataset(torch.utils.data.Dataset):
      def __init__(self, data:dict,num_classes:int,transform:dict,base:int):

            if num_classes == 2:
                  self.data = double_data(**data,**transform)
                  self.label = double_labels(**data)
            elif num_classes == 3:
                  self.data = triple_data(**data,**transform)
                  self.label = triple_labels(**data)
            elif num_classes == 4:
                  self.data = quad_data(**data,**transform)
                  self.label = quad_labels(**data)
            elif num_classes == base:
                  self.data = base_data(**data,**transform)
                  self.label = base_labels(**data)

            # self.label = F.one_hot(labels,num_classes=num_class).to(torch.float32)

      def __len__(self):
            return len(self.label)

      def __getitem__(self, index):
            X = self.data[index]
            y = self.label[index]
            return X, y
