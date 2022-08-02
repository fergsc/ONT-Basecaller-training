fast5="/path/to/read/fast5"

numPools=4

numReads=`echo "$(find $fast5 -name '*.fast5' | wc -l) $numPools" | awk '{print int($1/$2)}'`

for ((i = 1; i < $numPools; ++i))
do
    mkdir $i
    for file in `find $fast5 -name '*.fast5' | head -n $numReads`
    do
        mv $file $i
    done
done

mv $fast5 $numPools