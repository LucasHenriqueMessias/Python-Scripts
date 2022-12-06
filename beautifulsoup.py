from bs4 import BeautifulSoup
import codecs
with open('NF-LONG-SEP2022.MHTML', 'r') as f:
    soup = BeautifulSoup(f.read())
    tag = soup.select('td')
for i in tag:
    try:
        v_row_value = codecs.decode(i.text, 'hex').decode('utf-8')
        v_str_ini_pos = v_row_value.find("<chNFe>") + len("<chNFe>")
        v_str_end_pos = v_row_value.find("</chNFe>")
        v_xml_file = v_row_value[v_str_ini_pos: v_str_end_pos]
        v_file = open("C:\\Users\\goncalca\\Documents\\nfe\\September\\" +
                      v_xml_file + ".xml", "w", encoding="utf-8-sig")
        v_file.write(v_row_value)
        v_file.close()
    except Exception:
        pass
