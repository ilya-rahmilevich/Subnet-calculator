def validate_ip(ip_add):
    # check number of periods
    if ip_add.count(".") != 3:
      return False

    # check range of each number between periods
    for num in ip_add.split("."):
        if int(num) < 0 or int(num) > 255:
          return False

    return True

def cidr_to_netmask(cidr):
  mask = (0xffffffff >> (32 - cidr)) << (32 - cidr)
  return (str( (0xff000000 & mask) >> 24)   + '.' +
          str( (0x00ff0000 & mask) >> 16)   + '.' +
          str( (0x0000ff00 & mask) >> 8)    + '.' +
          str( (0x000000ff & mask)))

def netmask_to_cidr(netmask):
    negative_offset = 0

    for octet in netmask.split("."):
        binary = format(int(octet), '08b')
        for char in reversed(binary):
            if char == '1':
                break
            negative_offset += 1

    return '{0}'.format(32-negative_offset)

def number_of_hosts(cidr):
    return (1 << (32 - cidr)) - 2

def first_host(ip_add,netmask):
  num = [0,0,0,0]
  i = 0
  while i < len(ip_add.split(".")):
    num[i] = int(ip_add.split(".")[i]) & int(netmask.split(".")[i])
    i += 1
  num[len(num)-1] += 1
  return '.'.join(map(str, num))

def main():
  cidr=0
  netmask=0
  hosts=0
  first=""
  ip_address = input("Please enter an ip address with cidr: ")
  if validate_ip(ip_address.split("/")[0]) == False:
    print("Invalid address.")
  elif ip_address.split("/")[1].count(".") > 0 and validate_ip(ip_address.split("/")[1]) == False:
    print("Invalid address.")
  elif ip_address.split("/")[1].count(".") > 0:
    netmask=ip_address.split("/")[1]
    cidr=netmask_to_cidr(ip_address.split("/")[1])
  else:
    cidr=int(ip_address.split("/")[1])
    netmask=cidr_to_netmask(int(ip_address.split("/")[1]))

  if cidr != 0:
    hosts = number_of_hosts(cidr)
    first = first_host(ip_address.split("/")[0],netmask)

  print("Subnet mask: " + str(netmask))
  print("CIDR: " + str(cidr))
  print("Number of hosts: " + str(hosts))
  print("First IP: " + str(first))

if __name__ == '__main__':
  main()
