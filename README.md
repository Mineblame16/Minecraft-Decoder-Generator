# Minecraft Decoder Generator

This project is a Python script that generates a Minecraft decoder schematic using the `mcschematic` library. The script allows you to create a redstone decoder dynamically based on the number of bits you specify. It uses redstone wires, wool, redstone repeaters, and redstone torches to construct the decoder.

## Features
- Automatically generates a redstone decoder with a one-block gap between wires.
- Dynamically positions wires and components based on the number of bits.
- Saves the schematic in the format compatible with Minecraft Java Edition 1.20.

## Usage
1. **Install the required library**:
   - Install `mcschematic` using pip:
     ```bash
     pip install mcschematic
     ```

2. **Run the script**:
   - Modify the `n_bits` parameter in the `generate_decoder` function to specify the number of bits for the decoder.
   - Execute the script to generate the schematic:
     ```bash
     python decoder_generator.py
     ```

3. **Import the schematic into Minecraft**:
   - Use tools like WorldEdit or MCASelector to import the generated schematic (`decoder_with_gap.schem`) into your Minecraft world.

## Downsides
- **Repeaters**: You need to manually add repeaters after every 15 redstone wires to avoid signal loss.
- **Glass Towers**: Glass towers for vertical signal stacking need to be added manually. This can be done easily using tools like MCEdit.

## Recommended Workflow
1. Generate the decoder schematic using the script.
2. Use MCEdit or similar tools to:
   - Add repeaters every 15 redstone wires.
   - Add glass towers for vertical stacking if needed.
3. Save and import the modified schematic into your Minecraft world.

## Acknowledgments
Special thanks to **Sloimay**, the developer of the `mcschematic` library, for creating this incredible tool that made this project possible.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

