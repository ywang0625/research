import m5
import sys
import time

import argparse
from gem5.utils.override import overrides

from m5.objects import *
from m5.objects import Root
from gem5.utils.requires import requires
from gem5.coherence_protocol import CoherenceProtocol
from gem5.isas import ISA
from gem5.resources.resource import obtain_resource
from gem5.components.boards.x86_board import X86Board
from gem5.components.memory.multi_channel import DualChannelDDR4_2400
from gem5.components.processors.simple_switchable_processor import SimpleSwitchableProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.cachehierarchies.ruby.mesi_three_level_cache_hierarchy import MESIThreeLevelCacheHierarchy
#from gem5.utils.numa import RemoteChanneledMemory
from gem5.simulate.simulator import Simulator
from gem5.simulate.exit_event import ExitEvent

#Requirements
requires(
    isa_required = ISA.X86,
    coherence_protocol_required=CoherenceProtocol.MESI_THREE_LEVEL,
    kvm_required = True,
)


#Setting up for the benchmark
parser = argparse.ArgumentParser(
    description="An example configuration script to run the gapbs benchmarks."
)

gapbs_suite = obtain_resource(
    "gapbs-benchmark-suite", resource_version="1.0.0"
)

parser.add_argument(
    "--benchmark",
    type=str,
    required=True,
    help="Input the benchmark program to execute.",
    choices=[workload.get_id() for workload in gapbs_suite],
)

args = parser.parse_args()


#Processor (2 types of cores)
processor = SimpleSwitchableProcessor(
        starting_core_type = CPUTypes.KVM,
        switch_core_type = CPUTypes.TIMING,
        isa = ISA.X86,
        num_cores = 8,
)


# Set up the Ruby cache hierarchy
cache_hierarchy = MESIThreeLevelCacheHierarchy(
        l1i_size = "32kB",
        l1i_assoc = 8,
        l1d_size = "32kB",
        l1d_assoc = 8,
        l2_size = "256kB",
        l2_assoc = 16,
        l3_size = "8MB",
        l3_assoc = 16,
        num_l3_banks = 1,
)

#X86 board only suuportd 3GB of main memory
memory = DualChannelDDR4_2400(
        size = "3GB",
)

#I dont think there's a need for self def board
board = X86Board(
    clk_freq = "3GHz",
    processor = processor,
    memory = memory,
    cache_hierarchy = cache_hierarchy,
)




board.set_workload(obtain_resource(args.benchmark))



#Can edit later on 
def handle_workbegin():
    print("Resetting stats at the start of ROI...")
    m5.stats.reset()
    global start_tick
"configs/numa/x86_fs_first.py" 148L, 3612B                                                                                                                         1,1           Top
