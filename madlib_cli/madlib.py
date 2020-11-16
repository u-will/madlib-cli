def read_template(path):
  with open(path) as madlibFile:
    content = madlibFile.read()
    stripFile = content.strip()
  return stripFile


def parse_template(string_template):
  capturing = False
  dissected_string= ""
  part= []
  current_speech_part= ""
  for character in string_template:
    if not capturing:
      disssceted_string+= character

      if character == "{":
        capturing = True
    else:
      if character == "}":
        capturing = False
        part.append(current_speech_part)
        dissected_string += character
        current_speech_part =""
      else:
        current_speech_part += character
  return (dissected_string, parts)

def test_merge():
    actual = merge("A {} and {} {}.", ["dark", "stormy", "night"])
    expected = "A dark and stormy night."
    assert actual == expected

def merge(bare_template, responses):
  return bare_template.format(*responses)