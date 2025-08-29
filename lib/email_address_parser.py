import re

class EmailAddressParser:
	def __init__(self, addresses):
		self.addresses = addresses

	def parse(self):
		# Split by comma or whitespace
		parts = re.split(r'[\s,]+', self.addresses.strip())
		# Regex for a valid email address
		email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
		# Filter only valid emails
		emails = [email for email in parts if re.match(email_regex, email)]
		# Get unique and sort
		return sorted(set(emails))