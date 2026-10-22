Enterprise Ransomware Assessment & NIST CSF v2.0 Corporate Risk Register

Project:
Ransomware is one of the most critical threats facing modern enterprises. This project applies analytical workflows to model corporate risk distributions across an organization's architecture. It establishes an executive risk register directly mapped to the “NIST Cybersecurity Framework (CSF) v2.0 Core Functions”: Govern (GV), Identify (ID), Protect (PR), Detect (DE), Respond (RS), and Recover (RC).

Technologies and Libraries Used
* Python: Core scripting language used to build the automation engine.
* Pandas: Engineered data analysis library utilized for structuring datasets and running risk matrix logic computations.
* Openpyxl: Engine component backing custom Excel spreadsheet outputs.

Scoring System Architecture
The scoring system maps vulnerabilities onto a classic $5 \times 5$ Risk matrix ($Likelihood \times Impact = Score$):
* Inherent Risk Matrix**: Calculates overall threat levels before any defensive technical controls or tools are established.
* Residual Risk Matrix**: Represents calculated real risk exposure remaining after proposed mitigation pathways are successfully deployed.

Risk Level Ranges
* $\ge 15$**: Critical Risk
* $10$ to $14$**: High Risk
* $5$ to $9$**: Medium Risk
* $< 5$**: Low Risk

Step-by-Step Setup and Execution Instructions

1. Clone or Download Workspace Files
   Ensure all four required files are in your active project directory:
* `ransomware.py` (Script Logic)
* `requirements.txt` (Environment Mappings)
* `report.docx` (Complete Documentation)
* `README.md` (This file)

2. Environment Configuration
   Install the specified software dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Script Engine
   Execute the automated register compiler script:
   ```bash
   python YourName_ProjectName.py
   ```
   Running the code automatically compiles the mathematical indices and produces the project tracking file: `corporate_risk_register.xlsx`.

