#!/bin/zsh

#batch size
id_dir="/z/kiku/Dataset/ID"
src_dir="/z/kiku/Dataset/Target"

class=6
# #DIRECTORY CLEAN
# rm -rf $tar_dir/${IDlist}/*
# rm -rf $tar_dir/pytorch/*

#MAKE ID LIST
#python IDlist.py -t ${src_dir}/${positive} -o ${id_dir} -f $positive -cut ${cutlen}

##TRAIN
for i in 3000 4000 5000;do
    python main.py -t $id_dir -i $src_dir -class 6 -len $i -a Transformer -b 200 -me 30 -t_class 1
done

#python main.py -t $id_dir -i $src_dir -class 6 -len 3000 -b 100 -a LSTM -me 20 -hidden 64
#python main.py -t $id_dir -i $src_dir -class 6 -len 3000 -b 200 -a ResNet-me 20 -t_class 2
#python main.py -t $id_dir -i $src_dir -class 6 -len 5000 -b 200 -a Transformer -me 30 
#for j in 1 2 3 4 ;do
    #python main.py -t $id_dir -i $src_dir -class 6 -len 3000 -a ResNet -b 200 -me 30 -t_class $j
#done
