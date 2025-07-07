import mcschematic

def generate_decoder(n_bits):
    schem = mcschematic.MCSchematic()
    
    n_outputs = 2 ** n_bits

    for bit in range(n_bits):
        for output in range(n_outputs):
            binary = format(output, f"0{n_bits}b")
            
            x = 0
            y = -1 - bit * 2  # Offset by 2 for each bit
            z_main = output * 2  # Keep a 1-block gap for the main wires
            z_decoder = z_main + 1  # Decoder wires are placed 1 block next to the main wires
            
            # Main wires
            schem.setBlock((x, y, z_main), "minecraft:redstone_wire")
            schem.setBlock((x, y - 1, z_main), "minecraft:white_wool")
            
            # Decoder wires
            schem.setBlock((x, y, z_decoder), "minecraft:redstone_wire")
            schem.setBlock((x, y - 1, z_decoder), "minecraft:white_wool")
            
            if binary[bit] == "1":
                schem.setBlock((1, y - 1, z_decoder), "minecraft:redstone_wall_torch[facing=east]")
            else:
                schem.setBlock((1, y - 1, z_decoder), "minecraft:repeater[facing=west]")
            
            # Glass block for separation
            schem.setBlock((1, y - 2, z_decoder), "minecraft:white_stained_glass")
    
    # Save the schematic
    schem.save("./", "decoder", mcschematic.Version.JE_1_20)
    
generate_decoder(3)
