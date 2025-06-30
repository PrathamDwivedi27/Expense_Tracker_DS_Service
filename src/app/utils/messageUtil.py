import re

class MessageUtil:
    def isBankSms(self,message):
        words_to_search=[ "debited", "credited", "txn", "transaction",
                "account", "ac", "a/c", "amt", "balance",
                "card", "upi", "imps", "neft", "rtgs",
                "spent", "withdrawn", "withdrawal", "deposited",
                "salary", "statement", "limit",
                "payment", "loan", "emi", "ifsc", "acc",
                "bank", "cheque", "interest", "available",
                "funds", "transfer", "pos", "merchant",
                "atm", "netbanking", "ministatement", "charges",
                "processed", "remitter", "benificiary", "upi-ref", "mandate"]
        pattern = r'\b(?:' + '|'.join(re.escape(word) for word in words_to_search) + r')\b'
        return bool(re.search(pattern, message, flags=re.IGNORECASE))