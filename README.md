# Feeder Control

**Under development i just put something out there so that people can follow as i improve and upload more.**  

**BETA PCBs will be available soon message on Discord Info at the bottom.**

The **Feeder Control** board is an open-source controller designed to work seamlessly with the [Opulo Lumen PNP feeder design](https://opulo.io). This board allows for the simple use of a connector to individually control feeders without relying on a mandatory communication bus. Instead, it provides the option for a communication bus while also enabling simple direct connections. The USB-to-serial converter (**Feeder Commander**) is incredibly affordable, making this an ideal solution for a wide range of setups.  

## Key Features 

- **Simple Control**
  Simple low cost control via an io pin or serial is available. (Serial examples available after testing.) 
- **Feeder Bus**:  
  The Feeder Bus connector includes:  
  - 3.3V Bus  
  - 12V power  
  - Ground  
  - TX/RX for serial communication  
  - An additional customizable pin (e.g., for feeder activation or other functions).  

- **3.3V Bus**:  
  The 3.3V bus is **separate**, allowing you to regulate it once externally. This reduces the need for onboard switching power supplies or regulators, significantly lowering the cost per feeder. This also cuts down on heat dissipation, improving the overall efficiency of the board as well as giving the option of precise analogue control with a constant reference voltage.  

- **Optional Communication Bus**:  
  The communication bus functionality is available for machines that can easily integrate it, but it’s optional. This ensures flexibility for retrofitting machines where communication buses may not be practical or cost-effective. A USB controller is also available called the  **Feeder Commander**  

- **Ultra-Low-Cost Design**:  
  Designed from the ground up to keep costs low while making the Opulo feeder accessible to a wide range of machines. The 3.3V regulation and power efficiency are key factors in reducing costs without compromising functionality.  

- **Flexible and Compatible**:  
  - Retains the same connector locations for motors and other components as the Opulo Lumen PNP feeder board to ensure compatibility.  
  - The design is inspired by Opulo's feeder board in shape and certain features, but this is a completely original design tailored for use in my own pick-and-place machine.  
  - Perfect for interfacing the Opulo feeder with other machines and custom setups.  

- **12V Power**:  
  The board also includes **12V power** that can power the motor bus. While the 12V supply may potentially be adjustable, this needs to be confirmed through further testing, as it is primarily designed to support the motor.  

- **Analog Pin for Future Expansion**:  
  One of the features of the customizable pin, not used in the serial communication bus, has **analog capabilities**. This provides the opportunity for analog functions, which may be important for certain applications. While not all analog functions may be implemented in the firmware initially, the hardware is capable of supporting them.  

- **Feeder Control Test Utility**
  There is a test utility provided for testing the feeders and reading any communication from them.
  It is available in a Linux executable or a Python script I plan to create an executable for Windows and MacOS but i need to have access to these systems.

## Why This Board?  
I’m building my own pick-and-place machine based on the Opulo Lumen PNP. While Opulo's feeder controller is excellent, I designed the Feeder Control board to be simpler and to meet my specific needs. With this board, you can:  
- Interface the Opulo feeder with other pick-and-place machines.  
- Take advantage of the low-cost Feeder Commander USB-to-serial converter for communication.  

If you're looking for ultra-low-cost setups, the communication bus functionality is a great option, though it’s not required for general use.  

## Customization and Support  
I am happy to assist to the best of my ability and can create custom firmware upon request to meet specific needs. Whether you're working on a similar project or need help integrating the Feeder Control into your system, feel free to reach out.  

---

<div id="sales-button-placeholder">
  <a href="https://www.tindie.com/stores/aks/?ref=offsite_badges&utm_source=sellers_AKS&utm_medium=badges&utm_campaign=badge_small">
    <img src="https://d2ss6ovg47m0r5.cloudfront.net/badges/tindie-smalls.png" alt="I sell on Tindie" width="200" height="55">
  </a>
</div

---

## Contributions  
Contributions, feedback, and suggestions are welcome!  

---

This project is open-source, but it is important to acknowledge the influence of Opulo’s feeder design. Their work is the foundation for these advancements, and I’ve disclosed all relevant details about its inspiration and modifications.  

For any inquiries, please contact me via GitHub, [Discord](https://discord.com/channels/1316400333928267817/1316400333928267820) or submit an issue in the repository.

