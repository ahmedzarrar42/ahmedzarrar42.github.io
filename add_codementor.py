# Read the file
with open("index.html", "r") as f:
    content = f.read()

# Add Codementor link after the GitHub link block
old = '''          <a href="https://github.com/ahmedzarrar42" target="_blank" class="contact-link">
            <div class="contact-link-icon">🐙</div>
            github.com/ahmedzarrar42
          </a>'''

new = '''          <a href="https://github.com/ahmedzarrar42" target="_blank" class="contact-link">
            <div class="contact-link-icon">🐙</div>
            github.com/ahmedzarrar42
          </a>
          <a href="https://www.codementor.io/@muhammadahmed860797" target="_blank" class="contact-link">
            <div class="contact-link-icon">🎓</div>
            Codementor Profile
          </a>'''

if old in content:
    content = content.replace(old, new)
    with open("index.html", "w") as f:
        f.write(content)
    print("✅ Codementor link added successfully!")
else:
    print("❌ Could not find the GitHub link block — printing nearby content for debug:")
    idx = content.find("github.com/ahmedzarrar42")
    print(content[idx-200:idx+200])
