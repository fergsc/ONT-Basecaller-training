basecallingOutput="/path/to/bonito-basecalling/1 /path/to/bonito-basecalling/2" # eg. for multiple sub-devided training sets
basecallingOutput="/path/to/bonito-basecalling" # eg. for single training set

bonitoDir="/path/to/bonito"

cudaDevice="cuda:0"
epochs=12      # number of training cycles
batch_size=100 # number of training reads utilized in one iteration.
num_chunks=0   # Splits the reads into lengths of size X. 0 = don't split
learning_rate=4e-4 # Step size at each epoch
                   # to big = overshoot convergent point
                   # to small = slow learn.

# batch and chunk = resource optimisation.

first=1
for run in $basecallingOutput
do
    if [ $first == 1 ]
    then
        ${bonitoDir}/bonito train \
            --device $cudaDevice           \
            --epochs $epochs               \
            --lr $learning_rate            \
            --batch $batch_size            \
            --directory $run \
            $(basename $run)~trained
            #--chunks $num_chunks # using 0 -> dont need

        preRun=$(basename $run)~trained
        first=0
    else
        ${bonitoDir}/bonito train \
            --pretrained $preRun           \
            --device $cudaDevice           \
            --epochs $epochs               \
            --lr $learning_rate            \
            --batch $batch_size            \
            --directory $run \
            $(basename $run)~trained
            #--chunks $num_chunks # using 0 -> dont need

        preRun=$(basename $run)~trained
    fi
done