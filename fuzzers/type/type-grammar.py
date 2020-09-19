import gramfuzz
from gramfuzz.fields import *
import fuzz

class YRef(Ref):
    cat = "config_def"
class YDef(Def):
    cat = "config_def"

max_repeat = 2

Def("type", And(YRef("optsep"), YRef("module-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), "{", YRef("stmtsep"), YRef("type-stmt")), "}", cat="type")
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
YDef("type-stmt", And(YRef("type-keyword"), YRef("sep"), YRef("identifier-ref-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(YRef("type-body-stmts"), ""), "}")), YRef("stmtsep")))
YDef("type-keyword", "type")
YDef("identifier-ref-arg-str", YRef("identifier-ref-arg"))
YDef("identifier-ref-arg", YRef("identifier-ref"))
YDef("identifier-ref", And(Or(And(YRef("prefix"), ":"), ""), YRef("identifier")))
YDef("prefix", YRef("identifier"))
YDef("type-body-stmts", Or(YRef("numerical-restrictions"), YRef("decimal64-specification"), YRef("string-restrictions"), YRef("enum-specification"), YRef("leafref-specification"), YRef("identityref-specification"), YRef("instance-identifier-specification"), YRef("bits-specification"), YRef("union-specification"), YRef("binary-specification")))
YDef("numerical-restrictions", Or(YRef("range-stmt"), ""))
YDef("range-stmt", And(YRef("range-keyword"), YRef("sep"), YRef("range-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(YRef("error-message-stmt"), ""), Or(YRef("error-app-tag-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))
YDef("range-keyword", "range")
YDef("range-arg-str", YRef("range-arg"))
YDef("range-arg", And(YRef("range-part"), Or(Join(And(YRef("optsep"), "|", YRef("optsep"), YRef("range-part")), sep="", max=max_repeat), "")))
YDef("range-part", And(YRef("range-boundary"), Or(And(YRef("optsep"), "..", YRef("optsep"), YRef("range-boundary")), "")))
YDef("range-boundary", Or(YRef("min-keyword"), YRef("max-keyword"), YRef("decimal-value")))
YDef("min-keyword", "min")
YDef("max-keyword", "max")
YDef("decimal-value", And(YRef("integer-value"), ".", YRef("zero-integer-value")))
YDef("integer-value", Or(And("-", YRef("non-negative-integer-value")), YRef("non-negative-integer-value")))
YDef("non-negative-integer-value", Or("0", YRef("positive-integer-value")))
YDef("positive-integer-value", And(YRef("non-zero-digit"), Or(Join(YRef("DIGIT"), sep="", max=max_repeat), "")))
YDef("non-zero-digit", String(charset="123456789"))
YDef("zero-integer-value", Join(YRef("DIGIT"), sep="", max=max_repeat))
YDef("error-message-stmt", And(YRef("error-message-keyword"), YRef("sep"), YRef("string"), YRef("stmtend")))
YDef("error-message-keyword", "error-message")
YDef("string", YRef("yang-string"))
YDef("yang-string", Or(Join(YRef("yang-char"), sep="", max=max_repeat), ""))
YDef("yang-char", String(max=1))
YDef("stmtend", And(YRef("optsep"), Or(";", And("{", YRef("stmtsep"), "}")), YRef("stmtsep")))
YDef("error-app-tag-stmt", And(YRef("error-app-tag-keyword"), YRef("sep"), YRef("string"), YRef("stmtend")))
YDef("error-app-tag-keyword", "error-app-tag")
YDef("description-stmt", And(YRef("description-keyword"), YRef("sep"), YRef("string"), YRef("stmtend")))
YDef("description-keyword", "description")
YDef("reference-stmt", And(YRef("reference-keyword"), YRef("sep"), YRef("string"), YRef("stmtend")))
YDef("reference-keyword", "reference")
YDef("decimal64-specification", Or(And(YRef("fraction-digits-stmt"), Or(YRef("range-stmt"), "")), And(Or(YRef("range-stmt"), ""), YRef("fraction-digits-stmt"))))
YDef("fraction-digits-stmt", And(YRef("fraction-digits-keyword"), YRef("sep"), YRef("fraction-digits-arg-str"), YRef("stmtend")))
YDef("fraction-digits-keyword", "fraction-digits")
YDef("fraction-digits-arg-str", Or(And("1", Or(Or("0", "1", "2", "3", "4", "5", "6", "7", "8"), "")), "2", "3", "4", "5", "6", "7", "8", "9"))
YDef("string-restrictions", Or(And(Or(YRef("length-stmt"), ""), Or(Join(YRef("pattern-stmt"), sep="", max=max_repeat), "")), And(Or(Join(YRef("pattern-stmt"), sep="", max=max_repeat), ""), Or(YRef("length-stmt"), ""))))
YDef("length-stmt", And(YRef("length-keyword"), YRef("sep"), YRef("length-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(YRef("error-message-stmt"), ""), Or(YRef("error-app-tag-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))
YDef("length-keyword", "length")
YDef("length-arg-str", YRef("length-arg"))
YDef("length-arg", And(YRef("length-part"), Or(Join(And(YRef("optsep"), "|", YRef("optsep"), YRef("length-part")), sep="", max=max_repeat), "")))
YDef("length-part", And(YRef("length-boundary"), Or(And(YRef("optsep"), "..", YRef("optsep"), YRef("length-boundary")), "")))
YDef("length-boundary", Or(YRef("min-keyword"), YRef("max-keyword"), YRef("non-negative-integer-value")))
YDef("pattern-stmt", And(YRef("pattern-keyword"), YRef("sep"), YRef("string"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(YRef("modifier-stmt"), ""), Or(YRef("error-message-stmt"), ""), Or(YRef("error-app-tag-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))
YDef("pattern-keyword", "pattern")
YDef("modifier-stmt", And(YRef("modifier-keyword"), YRef("sep"), YRef("modifier-arg-str"), YRef("stmtend")))
YDef("modifier-keyword", "modifier")
YDef("modifier-arg-str", YRef("invert-match-keyword"))
YDef("invert-match-keyword", "invert-match")
YDef("enum-specification", Join(YRef("enum-stmt"), sep="", max=max_repeat))
YDef("enum-stmt", And(YRef("enum-keyword"), YRef("sep"), YRef("string"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), Or(YRef("value-stmt"), ""), Or(YRef("error-message-stmt"), ""), Or(YRef("error-app-tag-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))
YDef("enum-keyword", "enum")
YDef("if-feature-stmt", And(YRef("if-feature-keyword"), YRef("sep"), YRef("if-feature-expr-str"), YRef("stmtend")))
YDef("if-feature-keyword", "if-feature")
YDef("if-feature-expr-str", YRef("if-feature-expr"))
YDef("if-feature-expr", And(YRef("if-feature-term"), Or(And(YRef("sep"), YRef("or-keyword"), YRef("sep"), YRef("if-feature-expr")), "")))
YDef("if-feature-term", And(YRef("if-feature-factor"), Or(And(YRef("sep"), YRef("and-keyword"), YRef("sep"), YRef("if-feature-term")), "")))
YDef("if-feature-factor", Or(And(YRef("not-keyword"), YRef("sep"), YRef("if-feature-factor")), And("(", YRef("optsep"), YRef("if-feature-expr"), YRef("optsep"), ")"), YRef("identifier-ref-arg")))
YDef("not-keyword", "not")
YDef("and-keyword", "and")
YDef("or-keyword", "or")
YDef("value-stmt", And(YRef("value-keyword"), YRef("sep"), YRef("integer-value-str"), YRef("stmtend")))
YDef("value-keyword", "value")
YDef("integer-value-str", Or(And("-", YRef("non-negative-integer-value")), YRef("non-negative-integer-value")))
YDef("leafref-specification", Or(And(YRef("path-stmt"), Or(YRef("require-instance-stmt"), "")), And(Or(YRef("require-instance-stmt"), ""), YRef("path-stmt"))))
YDef("path-stmt", And(YRef("path-keyword"), YRef("sep"), YRef("path-arg-str"), YRef("stmtend")))
YDef("path-keyword", "path")
YDef("path-arg-str", YRef("path-arg"))
YDef("path-arg", Or(YRef("absolute-path"), YRef("relative-path")))
YDef("absolute-path", Join(And("/", YRef("node-identifier"), Or(Join(YRef("path-predicate"), sep="", max=max_repeat), "")), sep="", max=max_repeat))
YDef("node-identifier", And(Or(And(YRef("prefix"), ":"), ""), YRef("identifier")))
YDef("path-predicate", And("[", Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), "=", YRef("path-equality-expr"), Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), "]"))
YDef("path-equality-expr", And(YRef("node-identifier"), Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), "=", Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), YRef("path-key-expr")))
YDef("path-key-expr", And(YRef("current-function-invocation"), Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), "/", Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), YRef("rel-path-keyexpr")))
YDef("current-function-invocation", And(YRef("current-keyword"), Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), "(", Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), ")"))
YDef("current-keyword", "current")
YDef("rel-path-keyexpr", And(Join(And(".." ,Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), "/", Or(Join(YRef("WSP"), sep="", max=max_repeat), "")), sep="", max=max_repeat), Or(Join(And(YRef("node-identifier"), Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), "/", Or(Join(YRef("WSP"), sep="", max=max_repeat), "")), sep="", max=max_repeat), ""), YRef("node-identifier")))
YDef("CR", "")
YDef("relative-path", And(Join("../", sep="", max=max_repeat), YRef("descendant-path")))
YDef("descendant-path", And(YRef("node-identifier"), Or(And(Or(Join(YRef("path-predicate"), sep="", max=max_repeat), ""), YRef("absolute-path")), "")))
YDef("require-instance-stmt", And(YRef("require-instance-keyword"), YRef("sep"), YRef("require-instance-arg"), YRef("stmtend")))
YDef("require-instance-keyword", "require-instance")
YDef("require-instance-arg", Or(YRef("true-keyword"), YRef("false-keyword")))
YDef("true-keyword", "true")
YDef("false-keyword", "false")
YDef("identityref-specification", Join(YRef("base-stmt"), sep="", max=max_repeat))
YDef("base-stmt", And(YRef("base-keyword"), YRef("sep"), YRef("identifier-ref-arg-str"), YRef("stmtend")))
YDef("base-keyword", "base")
YDef("instance-identifier-specification", Or(YRef("require-instance-stmt"), ""))
YDef("bits-specification", Join(YRef("bit-stmt"), sep="", max=max_repeat))
YDef("bit-stmt", And(YRef("bit-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), Or(YRef("position-stmt"), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))
YDef("bit-keyword", "bit")
YDef("position-stmt", And(YRef("position-keyword"), YRef("sep"), YRef("position-value-arg-str"), YRef("stmtend")))
YDef("position-keyword", "position")
YDef("position-value-arg-str", YRef("non-negative-integer-value"))
YDef("status-stmt", And(YRef("status-keyword"), YRef("sep"), YRef("status-arg-str"), YRef("stmtend")))
YDef("status-keyword", "status")
YDef("status-arg-str", Or(YRef("current-keyword"), YRef("obsolete-keyword"), YRef("deprecated-keyword")))
YDef("obsolete-keyword", "obsolete")
YDef("deprecated-keyword", "deprecated")
YDef("union-specification", Join(YRef("type-stmt"), sep="", max=max_repeat))
YDef("binary-specification", Or(YRef("length-stmt"), ""))