# Run all benchmarks registed in sim_list/run_list.txt 
# Warmup 10M instructions and run 50M detailed instructions
# Usage: ./roll_5B.sh $BINARY_NAME

binary=$1
option=$2

while read trace
do
#	./djrunchamp.sh ${binary} 200 1000 ${trace} ${option} &
    ./run_champsim.sh ${binary} 200 1000 ${trace} ${option} &
done < sim_list/run_list.txt
