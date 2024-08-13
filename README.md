***2024 Undergraduate Summer Research***
**Table of Contents**
1. Overview
2. gem5 build process
3. Statistic
4. Important Matrix for stats.txt
5. Quick Access to Commands

**Overview of the Summer-Research folder**
In this folder consists of 4 folders: Report, Configuration Scripts, Source Codes, and Data.
In the Report folder consists a detailed report of the work done in summer. As there are lengthy code or data, they are stored in the other three folders depending on their file type. 
The files inside each folder are given a number for potential easier access, as they will be referenced in the report. 
Example: In the report, it says "run_simple.py locates at 1.0.1 in the Summer-Research folder". Then the script, run_simple.py will be located 1-Configuration-Scripts/1.0-gem5-scripts/1.0.1-run_simple. 
Note: The location inside the folder is different from the path that I ran in commands. 

**gem5 build process**
1. Download the dependenciees required based on your host system. The dependencies can be found here on the official website:
        https://www.gem5.org/documentation/general_docs/building#dependencies 
2. Clone the gem5 repository from Github using git
3. Use scons to build gem5 inside the gem5 folder
        scons build/{ISA}/gem5.{variant} -j{cpus on your platform}
4. It will take 40min ~ 1hr to finish your initial build. If your gem5 finished building, it will show this message:
        scons: done building targets.

**Statistic**
The statistics are located in m5out/stats.txt inside gem5 repository. The other files, such as config.ini, are list of every SimObject created for simulation and its respective values. 


**Important Matrix for stats.txt**
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
        scons build/{ISA}/gem5.{variant} -j{cpus on your platform}
   e.g.
        scons build/X86/gem5.opt -j5   
2. Run configuration scripts (simple)
        build/{ISA}/gem5.{variant} /path/to/your/config
