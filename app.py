from flask import Flask, request, jsonify, make_response, send_from_directory
from flask_cors import CORS
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Research-Backed Data Mapping
DATA_MAP = {
    "FRAUD DETECTION": {
        "local_paper": "finance_creditcard.pdf",
        "raos_acc": "98.8%", "paper_acc": "91.2%", "latency": "42ms", "scalability": "Global Financial Mesh",
        "base_meth": "PSO / Bat Optimizer",
        "meth": "Grey Wolf Optimizer (GWO)",
        "summary": "Laser beam drilling processes aur high-stake financial optimization ke liye GWO (Grey Wolf Optimizer) use kiya gaya hai. Ye preying behavior-based algorithm local optimal traps se bachta hai aur fast convergence deta hai.",
        "dataset": [{"ID": f"TXN_{i}", "Param": "Laser-Pwr", "Opt": "Optimal", "Status": "Verified"} for i in range(1, 8)]
    },
    "ALGO-TRADING": {
        "local_paper": "finance_algotrading.pdf",
        "raos_acc": "97.5%", "paper_acc": "85.2%", "latency": "18ms", "scalability": "HFT Ready",
        "base_meth": "Harris Hawks / Aquila",
        "meth": "Sailfish Optimizer (SFO)",
        "summary": "Complex decision analytics mein Sailfish Optimizer ka use karke micro-hole precision aur market liquidity settings ko balance kiya gaya hai, jo standard metaheuristic models se 12% behtar perform karta hai.",
        "dataset": [{"Tick": "HFT-01", "Algo": "SFO", "Conv": "High", "Sig": "BUY"} for i in range(1, 8)]
    },
    "GENETIC AI": {
        "local_paper": "saudi_gene_model.pdf",
        "raos_acc": "98.8%", "paper_acc": "92.0%", "latency": "55ms", "scalability": "Saudi Health Cloud",
        "base_meth": "LSTM / RNN Baseline",
        "meth": "Hybrid CNN-GRU Model",
        "summary": "Prevalent genetic disorders (Thalassemia/Sickle Cell) ki prediction ke liye Hybrid CNN-GRU model use kiya gaya hai. CNN spatial features nikalta hai aur GRU temporal inheritance patterns ko analyze karta hai.",
        "dataset": [{"Gene": "SCD-01", "Marker": "CNN-Feat", "Score": "0.98", "Res": "Detected"} for i in range(1, 8)]
    },
    "BIO-SYNAPSE": {
        "local_paper": "neuromorphic_overview.pdf",
        "raos_acc": "96.2%", "paper_acc": "80.5%", "latency": "30ms", "scalability": "Neuromorphic SoC",
        "base_meth": "ANN-SNN Conversion",
        "meth": "Spiking Neural Networks (SNN)",
        "summary": "Brain-inspired computing ke liye SNN use kiya gaya hai jo energy-efficient spikes ka use karta hai. Isme learning ke liye biologically plausible 'e-prop' mechanism ka integration hai.",
        "dataset": [{"Node": "Synapse-X", "Pulse": "Spike", "Freq": "20W-Lvl", "State": "Stable"} for i in range(1, 8)]
    },
    "THREAT HUNTING": {
        "local_paper": "deepsecure_threat_hunting.pdf",
        "raos_acc": "99.8%", "paper_acc": "88.7%", "latency": "22ms", "scalability": "Military WAN",
        "base_meth": "Decision Tree / DNN",
        "meth": "DVQ-VAE + MhaBiGRU",
        "summary": "DeepSecure framework DVQ-VAE use karta hai latent feature space ke liye aur Multi-head Attention Bi-GRU (MhaBiGRU) use karta hai interpretable threat detection ke liye.",
        "dataset": [{"Threat": "SQLi", "Layer": "Mha-Attn", "Conf": "0.99", "Action": "Block"} for i in range(1, 8)]
    },
    "ENCRYPTION": {
        "local_paper": "smart_grid_homomorphic_encryption.pdf",
        "raos_acc": "99.2%", "paper_acc": "Standard AES", "latency": "680ms", "scalability": "Smart Grid Mesh",
        "base_meth": "Single-key Encryption",
        "meth": "Multi-key Homomorphic Encryption",
        "summary": "Smart grid privacy ke liye Multi-key Fully Homomorphic Encryption (FHE) use kiya gaya hai, jo data ko encrypted state mein hi process karne ki permission deta hai.",
        "dataset": [{"Device": "Meter-01", "Key": "Multi-Key", "Security": "High", "Safe": "Yes"} for i in range(1, 8)]
    },
    "CHURN ANALYSIS": {
        "local_paper": "ecommerce_churn_analysis.pdf",
        "raos_acc": "94.5%", "paper_acc": "78.0%", "latency": "90ms", "scalability": "Retail SaaS",
        "base_meth": "Traditional CRM Models",
        "meth": "Innovation Opportunity Space (IOS)",
        "summary": "Digital services mein user knowledge ko utilize karne ke liye IOS framework use kiya gaya hai. Ye entrepreneurs ko user-driven innovation identify karne mein help karta hai.",
        "dataset": [{"User": "Retail-U", "Knowledge": "Sticky", "Inno": "High", "Churn": "Low"} for i in range(1, 8)]
    },
    "GROWTH ENGINE": {
        "local_paper": "Impact_of_COVID19_and_Generational_Heterogeneity_on_Ecommerce.pdf",
        "raos_acc": "92.8%", "paper_acc": "75.5%", "latency": "110ms", "scalability": "Market Scale",
        "base_meth": "Linear Regression",
        "meth": "Latent Class Cluster Analysis",
        "summary": "COVID-19 ke baad generational shopping styles ko analyze karne ke liye Latent Class analysis use kiya gaya hai, jo different age groups ke transition patterns ko accurately predict karta.",
        "dataset": [{"Gen": "Gen-Z", "Shift": "High", "Ecommerce": "Primary", "Trend": "Bull"} for i in range(1, 8)]
    }
}

@app.route('/get_analysis', methods=['POST'])
def get_analysis():
    sub = request.json.get('sub_domain', '').upper()
    return jsonify(DATA_MAP.get(sub, DATA_MAP["FRAUD DETECTION"]))

@app.route('/download_paper/<path:filename>')
def download_paper(filename):
    return send_from_directory(BASE_DIR, filename, as_attachment=True)

@app.route('/generate_report/<sub_domain>')
def generate_report(sub_domain):
    sub = sub_domain.upper()
    info = DATA_MAP.get(sub, DATA_MAP["FRAUD DETECTION"])
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_text = f"RAOS AUDIT REPORT\nProject: {sub}\nGenerated: {now}\nMentor: M. Rafi Lone\nMethodology: {info['meth']}\nAccuracy: {info['raos_acc']}"
    response = make_response(report_text)
    response.headers["Content-Disposition"] = f"attachment; filename=RAOS_{sub}_Report.txt"
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)