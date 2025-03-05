CIDR_to_MASK_TABLE = {
    "0": "0.0.0.0",
    "1": "128.0.0.0",
    "2": "192.0.0.0",
    "3": "224.0.0.0",
    "4": "240.0.0.0",
    "5": "248.0.0.0",
    "6": "252.0.0.0",
    "7": "254.0.0.0",
    "8": "255.0.0.0",
    "9": "255.128.0.0",
    "10": "255.192.0.0",
    "11": "255.224.0.0",
    "12": "255.240.0.0",
    "13": "255.248.0.0",
    "14": "255.252.0.0",
    "15": "255.254.0.0",
    "16": "255.255.0.0",
    "17": "255.255.128.0",
    "18": "255.255.192.0",
    "19": "255.255.224.0",
    "20": "255.255.240.0",
    "21": "255.255.248.0",
    "22": "255.255.252.0",
    "23": "255.255.254.0",
    "24": "255.255.255.0",
    "25": "255.255.255.128",
    "26": "255.255.255.192",
    "27": "255.255.255.224",
    "28": "255.255.255.240",
    "29": "255.255.255.248",
    "30": "255.255.255.252",
    "31": "255.255.255.254",
    "32": "255.255.255.255",
}
MASK_to_CIDR_TABLE = {
    "0.0.0.0": "0",
    "128.0.0.0": "1",
    "192.0.0.0": "2",
    "224.0.0.0": "3",
    "240.0.0.0": "4",
    "248.0.0.0": "5",
    "252.0.0.0": "6",
    "254.0.0.0": "7",
    "255.0.0.0": "8",
    "255.128.0.0": "9",
    "255.192.0.0": "10",
    "255.224.0.0": "11",
    "255.240.0.0": "12",
    "255.248.0.0": "13",
    "255.252.0.0": "14",
    "255.254.0.0": "15",
    "255.255.0.0": "16",
    "255.255.128.0": "17",
    "255.255.192.0": "18",
    "255.255.224.0": "19",
    "255.255.240.0": "20",
    "255.255.248.0": "21",
    "255.255.252.0": "22",
    "255.255.254.0": "23",
    "255.255.255.0": "24",
    "255.255.255.128": "25",
    "255.255.255.192": "26",
    "255.255.255.224": "27",
    "255.255.255.240": "28",
    "255.255.255.248": "29",
    "255.255.255.252": "30",
    "255.255.255.254": "31",
    "255.255.255.255": "32",
}


def class_calc(ip):
    a = ip.split(".")
    b = int(a[0])
    if 1 <= b <= 127:
        addr_class = "Class A"
    elif 128 <= b <= 191:
        addr_class = "Class B"
    elif 192 <= b <= 223:
        addr_class = "Class C"
    elif 224 <= b <= 239:
        addr_class = "Class D"
    elif 240 <= b <= 255:
        addr_class = "Class E"
    return addr_class


def default_mask_calc(addr_class):
    if addr_class == "Class A":
        subnet_mask = "255.0.0.0"
    elif addr_class == "Class B":
        subnet_mask = "255.255.0.0"
    elif addr_class == "Class C":
        subnet_mask = "255.255.255.0"
    elif addr_class == "Class D" or addr_class == "Class E":
        subnet_mask = "No default subnet mask"
    return subnet_mask


def CIDR(user_cidr):
    n_bits = user_cidr.replace("/", "")
    c_mask = CIDR_to_MASK_TABLE[n_bits]
    return c_mask, int(n_bits)


def network_bits_calc(user_needed_subnets):
    bit_calc = 0
    n_bits = 1
    while int(user_needed_subnets) > bit_calc:
        subnet_count_calc = (2 ** n_bits)
        if int(user_needed_subnets) > subnet_count_calc:
            n_bits += 1
        elif int(user_needed_subnets) < subnet_count_calc:
            break
    subnet_number_calc = 2 ** n_bits
    return subnet_count_calc, n_bits


def host_or_subnets(user_needed_subnets, user_needed_hosts):
    # host calc
    h_bit_count = 0
    total_host_number = 2 ** h_bit_count
    while total_host_number < int(user_needed_hosts):
        h_bit_count += 1
        total_host_number = 2 ** h_bit_count
    # subnet calc
    n_bit_calc = 0
    count = 1
    while int(user_needed_subnets) > n_bit_calc:
        subnet_count_calc = (2 ** count)
        if int(user_needed_subnets) > subnet_count_calc:
            count += 1
        elif int(user_needed_subnets) < subnet_count_calc:
            break
    subnet_number_calc = 2 ** count
    n_bits = count
    return total_host_number, h_bit_count, subnet_number_calc, n_bits


def host_bits_calc(user_needed_hosts):
    h_bit_count = 0
    total_host_number = 2 ** h_bit_count
    while total_host_number < int(user_needed_hosts):
        h_bit_count += 1
        total_host_number = 2 ** h_bit_count
    return h_bit_count, total_host_number


def main():
    user_ip_addr = input("Enter the IP address: ").strip().lower()
    user_cidr = input("Enter the CIDR notation or none: ").strip().lower()
    user_needed_hosts = input("Enter the required number of hosts or none: ").strip().lower()
    user_needed_subnets = input("Enter the required number of subnets or none: ").strip().lower()

    addr_class = class_calc(user_ip_addr)
    default_mask = default_mask_calc(addr_class)


    # CIDR Calc
    if user_cidr != "none" and user_needed_hosts == "none" and user_needed_subnets == "none":
        custom_mask, network_bits = CIDR(user_cidr)
        default_cidr = MASK_to_CIDR_TABLE[default_mask]
        custom_cidr = MASK_to_CIDR_TABLE[custom_mask]
        host_bits = 32 - int(network_bits)
        host_number_calc = (2 ** host_bits)
        host_usable_calc = host_number_calc - 2

        if addr_class == "Class A":
            working_bits = 24
            bits_borrowed = working_bits - host_bits
        elif addr_class == "Class B":
            working_bits = 16
            bits_borrowed = working_bits - host_bits
        elif addr_class == "Class C":
            working_bits = 8
            bits_borrowed = working_bits - host_bits

        subnet_number_calc = (2 ** bits_borrowed)

    # Host calc
    elif user_needed_hosts != "none" and user_cidr == "none" and user_needed_subnets == "none":
        host_bits, host_number_calc = host_bits_calc(user_needed_hosts)
        host_usable_calc = host_number_calc - 2
        default_cidr = MASK_to_CIDR_TABLE[default_mask]
        custom_cidr = 32 - host_bits

        custom_mask = CIDR_to_MASK_TABLE[str(custom_cidr)]

        if addr_class == "Class A":
            working_bits = 24
            bits_borrowed = working_bits - host_bits
            network_bits = bits_borrowed
        elif addr_class == "Class B":
            working_bits = 16
            bits_borrowed = working_bits - host_bits
            network_bits = bits_borrowed
        elif addr_class == "Class C":
            working_bits = 8
            bits_borrowed = working_bits - host_bits
            network_bits = bits_borrowed

        subnet_number_calc = (2 ** bits_borrowed)

    # Subnet Calc
    elif user_needed_subnets != "none" and user_cidr == "none" and user_needed_hosts == "none":
        subnet_number_calc, network_bits = network_bits_calc(user_needed_subnets)

        default_cidr = MASK_to_CIDR_TABLE[default_mask]

        custom_cidr = int(default_cidr) + network_bits
        custom_mask = CIDR_to_MASK_TABLE[str(custom_cidr)]
        host_bits = 32 - custom_cidr
        host_number_calc = (2 ** host_bits)
        host_usable_calc = (host_number_calc - 2)

        if addr_class == "Class A":
            working_bits = 24
            bits_borrowed = working_bits - host_bits
        elif addr_class == "Class B":
            working_bits = 16
            bits_borrowed = working_bits - host_bits
        elif addr_class == "Class C":
            working_bits = 8
            bits_borrowed = working_bits - host_bits

    #Host & Subnet Calc
    elif user_needed_hosts != "none" and user_needed_subnets != "none" and user_cidr == "none":
        host_number_calc, host_bits, subnet_number_calc, network_bits = host_or_subnets(user_needed_subnets,
                                                                                        user_needed_hosts)
        default_cidr = MASK_to_CIDR_TABLE[default_mask]
        custom_cidr = 32 - host_bits
        custom_mask = CIDR_to_MASK_TABLE[str(custom_cidr)]
        host_usable_calc = host_number_calc - 2
        if addr_class == "Class A":
            working_bits = 24
            bits_borrowed = working_bits - host_bits
        elif addr_class == "Class B":
            working_bits = 16
            bits_borrowed = working_bits - host_bits
        elif addr_class == "Class C":
            working_bits = 8
            bits_borrowed = working_bits - host_bits
   
    print(f"IP address: {user_ip_addr}")
    print(f"IP address class: {addr_class}")
    print(f"Default Mask: {default_mask}")
    print(f"Custom Mask: {custom_mask}")
    print(f"Default CIDR: /{default_cidr}")
    print(f"Custom CIDR: /{custom_cidr}")
    print(f"Number of Hosts: {host_number_calc}")
    print(f"Usable Hosts: {host_usable_calc}")
    print(f"Subnet Count: {subnet_number_calc}")
    print(f"Bits Borrowed: {bits_borrowed}")
    print(f"Network Bits: {network_bits}")
    print(f"Host Bits: {host_bits}")

if __name__ == "__main__":
    main()

