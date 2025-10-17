# imports
import psutil
import GPUtil
import platform
from datetime import datetime

# converts bytes to appropriate scaling
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
    
# collects system information 
def system_info():
 ("="*40, "System Information", "="*40)
 uname = platform.uname()
 (f"System: {uname.system}")
 (f"Node Name: {uname.node}")
 (f"Release: {uname.release}")
 (f"Version: {uname.version}")
 (f"Machine: {uname.machine}")
 (f"Processor: {uname.processor}")


# boot time
def boot_time():
 ("="*40, "Boot Time", "="*40)
 boot_time_timestamp = psutil.boot_time()
 bt = datetime.fromtimestamp(boot_time_timestamp)
 (f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")

def cpu_info():
# CPU Information
 ("="*40, "CPU Info", "="*40)
# number of cores
 ("Physical cores:", psutil.cpu_count(logical=False))
 ("Total cores:", psutil.cpu_count(logical=True))
# CPU frequencies
 cpufreq = psutil.cpu_freq()
 (f"Max Frequency: {cpufreq.max:.2f}Mhz")
 (f"Min Frequency: {cpufreq.min:.2f}Mhz")
 (f"Current Frequency: {cpufreq.current:.2f}Mhz")
# CPU usage
 ("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    (f"Core {i}: {percentage}%")
(f"Total CPU Usage: {psutil.cpu_percent()}%")

def memory_info():
# Memory Information
 ("="*40, "Memory Information", "="*40)
# get the memory details
svmem = psutil.virtual_memory()
(f"Total: {get_size(svmem.total)}")
(f"Available: {get_size(svmem.available)}")
(f"Used: {get_size(svmem.used)}")
(f"Percentage: {svmem.percent}%")
("="*20, "SWAP", "="*20)
# get the swap memory details (if exists)
swap = psutil.swap_memory()
(f"Total: {get_size(swap.total)}")
(f"Free: {get_size(swap.free)}")
(f"Used: {get_size(swap.used)}")
(f"Percentage: {swap.percent}%")

def disk_info():
# Disk Information
 ("="*40, "Disk Information", "="*40)
 ("Partitions and Usage:")
# get all disk partitions
partitions = psutil.disk_partitions()
for partition in partitions:
    (f"=== Device: {partition.device} ===")
    (f"  Mountpoint: {partition.mountpoint}")
    (f"  File system type: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        # this can be catched due to the disk that
        # isn't ready
        continue
    (f"  Total Size: {get_size(partition_usage.total)}")
    (f"  Used: {get_size(partition_usage.used)}")
    (f"  Free: {get_size(partition_usage.free)}")
    (f"  Percentage: {partition_usage.percent}%")
# get IO statistics since boot
disk_io = psutil.disk_io_counters()
(f"Total read: {get_size(disk_io.read_bytes)}")
(f"Total write: {get_size(disk_io.write_bytes)}")

def network_info():
# Network information
 ("="*40, "Network Information", "="*40)
# get all network interfaces (virtual and physical)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        (f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            (f"  IP Address: {address.address}")
            (f"  Netmask: {address.netmask}")
            (f"  Broadcast IP: {address.broadcast}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            (f"  MAC Address: {address.address}")
            (f"  Netmask: {address.netmask}")
            (f"  Broadcast MAC: {address.broadcast}")
# get IO statistics since boot
net_io = psutil.net_io_counters()
(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")


def get_host_data():
    data = {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent,
        "network_sent": psutil.net_io_counters().bytes_sent,
        "network_recv": psutil.net_io_counters().bytes_recv
    }
    return data
