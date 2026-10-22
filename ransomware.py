
IBM SkillsBuild Data Analytics with AI Academic Internship Program
Project: Enterprise Ransomware Assessment & Corporate Risk Register
File Name: YourName_ProjectName.py
Description: Automates the creation, matrix computation (Likelihood x Impact), and 
             NIST CSF v2.0 mapping of an enterprise ransomware risk register.


import pandas as pd
import os

def calculate_risk(likelihood, impact):
    return likelihood * impact

def categorize_risk(score):
    if score >= 15:
        return "Critical"
    elif score >= 10:
        return "High"
    elif score >= 5:
        return "Medium"
    else:
        return "Low"

def main():
    print("Initializing Enterprise Ransomware Assessment...")
    
    # Core Risk Matrix Dataset mapped directly to NIST CSF v2.0 Functions
    risk_data = [
        {
            "Risk_ID": "RSK-ID-01",
            "NIST_CSF_Function": "Govern (GV)",
            "Risk_Description": "Lack of comprehensive ransomware governance policies and third-party risk assessments leads to unmonitored vendor vulnerabilities.",
            "Inherent_Likelihood": 4,
            "Inherent_Impact": 5,
            "Targeted_Mitigation_Control": "Establish an executive-backed Cybersecurity Governance framework and implement mandatory third-party vendor risk assessment questionnaires.",
            "Residual_Likelihood": 2,
            "Residual_Impact": 4
        },
        {
            "Risk_ID": "RSK-ID-02",
            "NIST_CSF_Function": "Identify (ID)",
            "Risk_Description": "Incomplete IT asset inventory hides shadow IT software and unpatched legacy hardware vulnerable to exploit kits.",
            "Inherent_Likelihood": 5,
            "Inherent_Impact": 4,
            "Targeted_Mitigation_Control": "Deploy automated asset discovery tooling and map all data retention stores containing sensitive information.",
            "Residual_Likelihood": 2,
            "Residual_Impact": 4
        },
        {
            "Risk_ID": "RSK-ID-03",
            "NIST_CSF_Function": "Protect (PR)",
            "Risk_Description": "Phishing vector success resulting from missing multi-factor authentication (MFA) parameters across cloud infrastructure portals.",
            "Inherent_Likelihood": 5,
            "Inherent_Impact": 5,
            "Targeted_Mitigation_Control": "Enforce Phishing-resistant MFA universally, implement strict email endpoint filtering, and run phishing simulation updates.",
            "Residual_Likelihood": 2,
            "Residual_Impact": 3
        },
        {
            "Risk_ID": "RSK-ID-04",
            "NIST_CSF_Function": "Detect (DE)",
            "Risk_Description": "Ransomware execution occurs undetected in real-time due to missing centralized logging and incomplete EDR alert coverage.",
            "Inherent_Likelihood": 4,
            "Inherent_Impact": 5,
            "Targeted_Mitigation_Control": "Integrate an Endpoint Detection and Response (EDR) system feeding logs directly into a 24/7 Security Operations Center SIEM platform.",
            "Residual_Likelihood": 1,
            "Residual_Impact": 5
        },
        {
            "Risk_ID": "RSK-ID-05",
            "NIST_CSF_Function": "Respond (RS)",
            "Risk_Description": "Delayed mitigation reaction or improper network containment during an incident, accelerating cross-network data encryption.",
            "Inherent_Likelihood": 4,
            "Inherent_Impact": 4,
            "Targeted_Mitigation_Control": "Draft specific ransomware playbook procedures, perform table-top disaster simulation exercises, and deploy isolated network segments.",
            "Residual_Likelihood": 2,
            "Residual_Impact": 2
        },
        {
            "Risk_ID": "RSK-ID-06",
            "NIST_CSF_Function": "Recover (RC)",
            "Risk_Description": "System restores fail or take too long because primary on-site backups are encrypted alongside standard corporate infrastructure logs.",
            "Inherent_Likelihood": 3,
            "Inherent_Impact": 5,
            "Targeted_Mitigation_Control": "Implement automated 3-2-1 backup policies containing immutable, isolated, air-gapped cloud target repositories.",
            "Residual_Likelihood": 1,
            "Residual_Impact": 2
        }
    ]
    
    # Dataframe construction and dynamic matrix scoring
    df = pd.DataFrame(risk_data)
    
    df["Inherent_Risk_Score"] = df.apply(lambda row: calculate_risk(row["Inherent_Likelihood"], row["Inherent_Impact"]), axis=1)
    df["Inherent_Risk_Level"] = df["Inherent_Risk_Score"].apply(categorize_risk)
    
    df["Residual_Risk_Score"] = df.apply(lambda row: calculate_risk(row["Residual_Likelihood"], row["Residual_Impact"]), axis=1)
    df["Residual_Risk_Level"] = df["Residual_Risk_Score"].apply(categorize_risk)
    
    # Organize column view order
    ordered_columns = [
        "Risk_ID", "NIST_CSF_Function", "Risk_Description", 
        "Inherent_Likelihood", "Inherent_Impact", "Inherent_Risk_Score", "Inherent_Risk_Level",
        "Targeted_Mitigation_Control", 
        "Residual_Likelihood", "Residual_Impact", "Residual_Risk_Score", "Residual_Risk_Level"
    ]
    df = df[ordered_columns]
    
    # File save execution
    output_filename = "corporate_risk_register.xlsx"
    df.to_excel(output_filename, index=False)
    print(f"Success! Risk register successfully compiled and exported to file: '{output_filename}'")

if __name__ == "__main__":
    main()

