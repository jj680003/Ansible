import ipaddress

# Define the starting subnet (adjust as needed)
network = ipaddress.IPv4Network('10.0.0.0/16')

# Open the file to write the subnets
with open('available_subnets.yml', 'w') as f:
    f.write("available_subnets:\n")
    
    # Generate the first 200 /24 subnets
    subnets = list(network.subnets(new_prefix=24))[:200]
    
    # Write each subnet into the YAML file
    for subnet in subnets:
        f.write(f"  - {subnet}\n")

print("200 subnets have been generated and saved to available_subnets.yml")
