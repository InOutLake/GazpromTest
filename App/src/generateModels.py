import subprocess
from config import DATABASE_URL

command = ['sqlacodegen', DATABASE_URL]
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print("Command output:", result.stdout.decode())
print("Command error:", result.stderr.decode())