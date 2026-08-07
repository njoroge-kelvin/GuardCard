# GuardCard

GuardCard is a compliance-first RESTful API service designed to act as a core dispute management system for modern merchants and payment gateways. It streamlines chargeback workflows while strictly adhering to card network rules and data security standards.

---

##  Core Features & Compliance Implementation

### PCI DSS Tokenization & Storage
* **Zero Plaintext PANs:** The system strictly forbids storing raw Primary Account Numbers (PANs).
* **Isolated Tokenizer Engine:** A dedicated module ingests mock PANs and returns secure tokens.
* **Cryptographic Security:** Cards are secured using AES-256 encryption alongside strict Key Management practices.

### Reason Code Rules Engine
* **Automated Mapping:** Maps incoming dispute claims to official card network regulatory codes.
* **Visa Support:** Identifies and assigns codes like **Visa 10.4 (Other Fraud)**.
* **Mastercard Support:** Identifies and assigns codes like **Mastercard 4837 (No Cardholder Authorization)**.

### Compelling Evidence Processor
* **Merchant Defense Workflows:** Allows users to upload critical evidence files (e.g., receipts, digital tracking logs).
* **Pre-Submission Validation:** Evaluates uploads against Mastercard and Visa **"Compelling Evidence 3.0"** requirements before submitting to the network.

---

### Technical Architecture

### Backend Stack Options
* **Node.js** (TypeScript)
* **Python** (FastAPI)
* **Java** (Spring Boot)

### Security & Cryptography
* **Data at Rest:** Native crypto libraries for robust AES-256 encryption.
* **Authentication:** Bcrypt for secure user password and credential hashing.

### Database Engine
* **Supported Systems:** PostgreSQL or MongoDB.
* **State Machine:** Tracks complete dispute life cycles across key states: `Open`, `Under Review`, `Won`, and `Lost`.
