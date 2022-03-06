CFG="bonitoi-trained-model.cfg"
fast5Dir="/path/to/fast5"
cudaDevice="cuda:0"
guppyPath="/path/to/guppyh"

[ -d guppyOutput ] && rm -r guppyOutput
mkdir guppyOutput

${guppyPath}/guppy_basecaller \
    -c $CFG                   \
    --input_path $fast5Dir    \
    --save_path guppyOutput   \
    --records_per_fastq 0     \
    --device $cudaDevice      \
    --recursive               \
    --disable_pings           \
    --disable_qscore_filtering

find guppyOutput -name '*.fastq'  | xargs cat | pigz -p $threads > $(basename $fast5Dir).fastq.gz
cp guppyOutput/*.txt .
rm -r guppyOutput