import gramfuzz
from gramfuzz.fields import *
import fuzz

class YRef(Ref):
    cat = "config_def"
class YDef(Def):
    cat = "config_def"

max_repeat = 2

Def("import", And(YRef("optsep"), YRef("module-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), "{", YRef("stmtsep"), YRef("import-stmt")), "}", cat="import")
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
YDef("import-stmt", And(YRef("import-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), YRef("prefix-stmt"), Or(";", Or(And("{", YRef("stmtsep"), Or(YRef("revision-date-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}"), And("{", YRef("stmtsep"), Or(YRef("revision-date-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(YRef("description-stmt"), ""), "}"), And("{", YRef("stmtsep"), Or(YRef("reference-stmt"), ""), Or(YRef("revision-date-stmt"), ""), Or(YRef("description-stmt"), ""), "}"), And("{", YRef("stmtsep"), Or(YRef("reference-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("revision-date-stmt"), ""), "}"), And("{", YRef("stmtsep"), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(YRef("revision-date-stmt"), ""), "}"), And("{", YRef("stmtsep"), Or(YRef("description-stmt"), ""), Or(YRef("revision-date-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), ), YRef("stmtsep")))
YDef("import-keyword", "import")
YDef("prefix-stmt", And(YRef("prefix-keyword"), YRef("sep"), YRef("prefix-arg-str"), YRef("stmtend")))
YDef("prefix-keyword", "prefix")
YDef("prefix-arg-str", YRef("prefix-arg"))
YDef("prefix-arg", YRef("prefix"))
YDef("prefix", YRef("identifier"))
YDef("stmtend", And(YRef("optsep"), Or(";", And("{", YRef("stmtsep"), "}")), YRef("stmtsep")))
YDef("revision-date-stmt", And(YRef("revision-date-keyword"), YRef("sep"), YRef("revision-date"), YRef("stmtend")))
YDef("revision-date-keyword", "revision-date")
YDef("revision-date", YRef("date-arg-str"))
YDef("date-arg-str", YRef("date-arg"))
YDef("date-arg", And(YRef("DIGIT"), YRef("DIGIT"), YRef("DIGIT"), YRef("DIGIT"), "-", YRef("DIGIT"), YRef("DIGIT"), "-", YRef("DIGIT"), YRef("DIGIT")))
YDef("description-stmt", And(YRef("description-keyword"), YRef("sep"), YRef("string"), YRef("stmtend")))
YDef("description-keyword", "description")
YDef("string", YRef("yang-string"))
YDef("yang-string", Or(Join(YRef("yang-char"), sep="", max=max_repeat), ""))
YDef("yang-char", String(max=1))
YDef("reference-stmt", And(YRef("reference-keyword"), YRef("sep"), YRef("string"), YRef("stmtend")))
YDef("reference-keyword", "reference")
