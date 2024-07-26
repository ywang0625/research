***Output Files (July 26, 2024)***

**gem5 build process**

*Note:
        (1) The processes are specifically executed with gem5 v24.0.0.0
        (2) Steps 1 - 4 are for gapbs benchmark, skip to step 5 for building gem5

1. After cloning the gem5-resource repoistory, clone the gem5 repository specifically in src/gapbs/. 
2. Chaging directory to src/gapbs/gem5/util/m5, we need to create m5 because it is required to create disk image. Below is the command: 
        scons build/x86/out/m5
3. To create disk image, we need to add the packer binary in the disk-image directory. Firstly, go back to /src/gapbs/, and create the directory http inside disk-image
        cd disk-image/
        mkdir http
        touch http/dummy.txt
   Without the directory http, when we're building the disk image we can run into error saying http directory not found
4. We run the command to download packer binary and build disk-image
        ./build.sh

5. To build gem5, scons is used. The following is the syntax to build gem5
        scons build/{ISA}/gem5.{variant} - j {cpus}
   {variant} specifies the compilation setting, and opt is a build variant that has optimizations and run time debugging support. {cpus} specifies the number of threads.
   The command that is used for this experiment is the following: 
        scons build/X86_MESI_THREE_LEVEL/gem5.opt -j8
   MESI_Three_Level is the cache coherence protocol. After running the command, the compilationis finished and there will be the working gem5 executable. 
6. To run the configuration script, run the following command
        build/X86_MESI_THREE_LEVEL/gem5.opt /path/to/your/config --benchmark {gapbs}
   The benchmark supports the following types:  {gapbs-cc-test,gapbs-cc-small,gapbs-cc-medium,gapbs-bc-test,gapbs-bc-small,gapbs-bc-medium,gapbs-tc-test,gapbs-tc-small,gapbs-tc-medium,gapbs-pr-test,gapbs-pr-small,gapbs-pr-medium,gapbs-bfs-test,gapbs-bfs-small,gapbs-bfs-medium}




**Important Matrix**
*Cache*
1. For cache demand hit, miss, and access, search the following key words:
       demand_hits
       demand_misses
       demand_accesses
   After the "...cache_hierarchy.ruby_system." it should display which layer of cache this is for. If it's for L3, it will display "l3_controllers"

   In the ruby backend, L0Cache is L1 cache in stdlib, which is why there are some L0 cache in there. In addition, for example, after "L0Cache_Controller" there might be a few letters, such as "IS". They are the states and each have different purpose. Please visit here for more detailed description: https://www.gem5.org/documentation/general_docs/ruby/MESI_Two_Level/. Unfortuntately, there isn't a document for Mesi_three_level, but it should be similar. 

*Memory*
1. 'mem_ctrl' is for memory controller statistics, and 'dram' is for DRAM-specific metrics. 
2. to find bandwidth, either it contains 'bw' or have the description on the side



**Quick Access to Commands**
1. Building gem5
        scons build/X86_MESI_THREE_LEVEL/gem5.opt -j8
2. Running the configuration script with the benchmark
        build/X86_MESI_THREE_LEVEL/gem5.opt /path/to/your/config --benchmark {insert-gapbs-benchmark-here}
