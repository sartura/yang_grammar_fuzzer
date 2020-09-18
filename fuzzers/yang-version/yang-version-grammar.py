import gramfuzz
from gramfuzz.fields import *
import fuzz

class YRef(Ref):
    cat = "config_def"
class YDef(Def):
    cat = "config_def"

max_repeat = 2

Def("yang-version", And(YRef("optsep"), YRef("module-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), "{", YRef("stmtsep"), YRef("yang-version-stmt")), "}", cat="yang-version")
YDef("optsep", Or(Join(Or(YRef("WSP"), YRef("line-break")), sep="", max=max_repeat), ""))
YDef("WSP", Or(YRef("SP"), YRef("HTAB")))
YDef("SP", " ")
YDef("HTAB", "\t")
YDef("line-break", Or(YRef("CRLF"), YRef("LF")))
YDef("CRLF", And(YRef("CR"), YRef("LF")))
YDef("CR", "")
YDef("LF", "\n")
YDef("module-keyword", "module")
YDef("sep", Join(Or(YRef("WSP"), YRef("line-break")), sep="", max=max_repeat))
YDef("identifier-arg-str", YRef("identifier-arg"))
YDef("identifier-arg", YRef("identifier"))
YDef("identifier", And(Or(YRef("ALPHA"), "_"), Or(Join(Or(YRef("ALPHA"), YRef("DIGIT"), "_", "-", "."), sep="", max=max_repeat), "")))
YDef("ALPHA", String(charset=String.charset_alpha))
YDef("DIGIT", String(charset="0123456789"))
YDef("stmtsep", Or(Join(Or(YRef("WSP"), YRef("line-break")), sep="", max=max_repeat), ""))
YDef("yang-version-stmt", And(YRef("yang-version-keyword"), YRef("sep"), YRef("yang-version-arg"), YRef("stmtend")))
YDef("yang-version-keyword", "yang-version")
YDef("yang-version-arg", "1.1")
YDef("stmtend", And(YRef("optsep"), Or(";", And("{", YRef("stmtsep"), "}")), YRef("stmtsep")))
