# OmniHunter-v1.0
Multi-Service Combo-Based Cracker A powerful, high-speed automated tool designed to extract and verify access from Email:Pass Combo Lists. This tool intelligently parses combos to hunt for multiple types of access, including Mail Servers, Hosting Panels, and CMS platforms.
🚀 Core Functionality
The tool takes a standard email:password list and performs a "Deep Check" by attempting to crack:
SMTP Servers: Automatically identifies the host from the email domain and tests common ports (465, 587, 25) to find working mail senders.
cPanel & WHM: Bruteforces hosting management panels by generating smart usernames derived from the domain name.
WordPress Admin: Targets the /wp-login.php of the associated domain to gain CMS access.
🛠 Technical Highlights
All-in-One Cracking: One combo can be tested against 5+ different services simultaneously.

Smart Domain Parsing: Extracts the root domain and mail server host automatically from any email format.

Advanced Threading: Powered by a multiprocessing pool to handle thousands of combos in minutes.

Success Logging: Separates "GOOD" hits into organized files: SMTPs.txt, WebMail.txt, cPanels.txt, and Successfully_logged_WordPress.txt.
📖 Usage
1Prepare your combo.txt in the format email@domain.com:password.

2Run the script:
Bash
python main.py combo.txt
Requirements:
requests
colorama
tabulate
