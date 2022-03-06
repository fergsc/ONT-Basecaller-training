basecallingOutput="/path/to/bonito-basecalling"
bonitoDir="/path/to/bonito"

cudaDevice="cuda:0"
epochs=15      # number of training cycles
batch_size=100 # number of training reads utilized in one iteration.
num_chunks=0   # Splits the reads into lengths of size X. 0 = don't split
learning_rate=4e-4 # tuning parameter for optimization of learning algorithm.
                   # Step size at each epoch
                   # to big = overshoot convergent point
                   # to small = slow learn.

# batch and chunk = resource optimisation.


${bonitoDir}/bonito train \
    --device $cudaDevice           \
    --epochs $epochs               \
    --lr $learning_rate            \
    --batch $batch_size            \
    --directory $basecallingOutput \
    $(basename $basecallingOutput)~trained

#--chunks $num_chunks # using 0 -> dont need

