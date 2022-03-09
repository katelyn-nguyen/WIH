from PyPDF2 import PdfFileReader

filename = "flusummary_2022_wk07-030322final.pdf"
contents = []
idx = 0

with open(filename, 'rb') as f:
    reader = PdfFileReader(f)
    contents = reader.getPage(0).extractText()
    contents = ' '.join(contents.split())
    idx_start = contents.find("Reported This Week")
    idx_end = contents.find("Influenza - associated Deaths")

line = contents[idx_start:idx_end].split(":")
for i in range(len(line)):
    line[i] = line[i].strip()

line = line[1::]
line[0] = line[0].split(" ")[0]

reported_this_week = line[0]
season_to_date = line[1]

print(f"Reported this week: {reported_this_week:}")
print(f"Infections this season: {season_to_date:}")