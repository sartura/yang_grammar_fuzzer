import gramfuzz
from gramfuzz.fields import *
import fuzz

class YRef(Ref):
    cat = "config_def"
class YDef(Def):
    cat = "config_def"

max_repeat = 2

# for now generate only modules
Def("yang", YRef("module-stmt"), cat="yang")
#Def("yang", Or(YRef("module-stmt"), YRef("submodule-stmt")), cat="yang")

YDef("module-stmt", And(YRef("optsep"), YRef("module-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), "{", YRef("stmtsep"), YRef("module-header-stmts"), YRef("linkage-stmts"), YRef("meta-stmts"), YRef("revision-stmts"), YRef("body-stmts"), "}", YRef("optsep")))

YDef("submodule-stmt", And(YRef("optsep"), YRef("submodule-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), "{", YRef("stmtsep"), YRef("submodule-header-stmts"), YRef("linkage-stmts"), YRef("meta-stmts"), YRef("revision-stmts"), YRef("body-stmts"), "}", YRef("optsep")))

YDef("module-header-stmts", Or(And(YRef("yang-version-stmt"), YRef("namespace-stmt"), YRef("prefix-stmt")), And(YRef("yang-version-stmt"), YRef("prefix-stmt"), YRef("namespace-stmt")), And(YRef("namespace-stmt"), YRef("yang-version-stmt"), YRef("prefix-stmt")), And(YRef("namespace-stmt"), YRef("prefix-stmt"), YRef("yang-version-stmt")), And(YRef("prefix-stmt"), YRef("yang-version-stmt"), YRef("namespace-stmt")), And(YRef("prefix-stmt"), YRef("namespace-stmt"), YRef("yang-version-stmt"))))

YDef("submodule-header-stmts", Or(And(YRef("yang-version-stmt"), YRef("belongs-to-stmt")), And(YRef("belongs-to-stmt"), YRef("yang-version-stmt"))))

YDef("meta-stmts", Or(And(Or(YRef("organization-stmt"), ""), Or(YRef("contact-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), "")), \
                  And(Or(YRef("organization-stmt"), ""), Or(YRef("contact-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(YRef("description-stmt"), "")), \
                  And(Or(YRef("organization-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(YRef("contact-stmt"), ""), Or(YRef("description-stmt"), "")), \
                  And(Or(YRef("organization-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("contact-stmt"), "")), \
                  And(Or(YRef("organization-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(YRef("contact-stmt"), "")), \
                  And(Or(YRef("organization-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("contact-stmt"), ""), Or(YRef("reference-stmt"), "")), \
                  And(Or(YRef("contact-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("organization-stmt"), ""), Or(YRef("reference-stmt"), "")), \
                  And(Or(YRef("contact-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(YRef("organization-stmt"), "")), \
                  And(Or(YRef("contact-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("organization-stmt"), "")), \
                  And(Or(YRef("contact-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(YRef("organization-stmt"), ""), Or(YRef("description-stmt"), "")), \
                  And(Or(YRef("contact-stmt"), ""), Or(YRef("organization-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(YRef("description-stmt"), "")), \
                  And(Or(YRef("contact-stmt"), ""), Or(YRef("organization-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), "")), \
                  And(Or(YRef("reference-stmt"), ""), Or(YRef("organization-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("contact-stmt"), "")), \
                  And(Or(YRef("reference-stmt"), ""), Or(YRef("organization-stmt"), ""), Or(YRef("contact-stmt"), ""), Or(YRef("description-stmt"), "")), \
                  And(Or(YRef("reference-stmt"), ""), Or(YRef("contact-stmt"), ""), Or(YRef("organization-stmt"), ""), Or(YRef("description-stmt"), "")), \
                  And(Or(YRef("reference-stmt"), ""), Or(YRef("contact-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("organization-stmt"), "")), \
                  And(Or(YRef("reference-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("contact-stmt"), ""), Or(YRef("organization-stmt"), "")), \
                  And(Or(YRef("reference-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("organization-stmt"), ""), Or(YRef("contact-stmt"), "")), \
                  And(Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(YRef("organization-stmt"), ""), Or(YRef("contact-stmt"), "")), \
                  And(Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(YRef("contact-stmt"), ""), Or(YRef("organization-stmt"), "")), \
                  And(Or(YRef("description-stmt"), ""), Or(YRef("contact-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(YRef("organization-stmt"), "")), \
                  And(Or(YRef("description-stmt"), ""), Or(YRef("contact-stmt"), ""), Or(YRef("organization-stmt"), ""), Or(YRef("reference-stmt"), "")), \
                  And(Or(YRef("description-stmt"), ""), Or(YRef("organization-stmt"), ""), Or(YRef("contact-stmt"), ""), Or(YRef("reference-stmt"), "")), \
                  And(Or(YRef("description-stmt"), ""), Or(YRef("organization-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(YRef("contact-stmt"), ""))))

YDef("linkage-stmts", Or(And(Or(Join(YRef("import-stmt"), sep="", max=max_repeat), ""), Or(YRef("include-stmt"), sep="", max=max_repeat)), And(Or(Join(YRef("include-stmt"), sep="", max=max_repeat), ""), Or(YRef("import-stmt"), sep="", max=max_repeat))))

YDef("revision-stmts", Or(Join(YRef("revision-stmt"), sep="", max=max_repeat), ""))

YDef("body-stmts", Or(Join(Or(YRef("extension-stmt"), YRef("feature-stmt"), YRef("identity-stmt"), YRef("typedef-stmt"), YRef("grouping-stmt"), YRef("data-def-stmt"), YRef("augment-stmt"), YRef("rpc-stmt"), YRef("notification-stmt"), YRef("deviation-stmt")), sep="", max=max_repeat), ""))

YDef("data-def-stmt", Or(YRef("container-stmt"), YRef("leaf-stmt"), YRef("leaf-list-stmt"), YRef("list-stmt"), YRef("choice-stmt"), YRef("anydata-stmt"), YRef("anyxml-stmt"), YRef("uses-stmt")))

YDef("yang-version-stmt", And(YRef("yang-version-keyword"), YRef("sep"), YRef("yang-version-arg"), YRef("stmtend")))

YDef("yang-version-arg", "1.1")

YDef("import-stmt", And(YRef("import-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), Or(";", \

    Or(And("{", YRef("stmtsep"), Or(YRef("revision-date-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}"), \
    And("{", YRef("stmtsep"), Or(YRef("revision-date-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(YRef("description-stmt"), ""), "}"), \
    And("{", YRef("stmtsep"), Or(YRef("reference-stmt"), ""), Or(YRef("revision-date-stmt"), ""), Or(YRef("description-stmt"), ""), "}"), \
    And("{", YRef("stmtsep"), Or(YRef("reference-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("revision-date-stmt"), ""), "}"), \
    And("{", YRef("stmtsep"), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(YRef("revision-date-stmt"), ""), "}"), \
    And("{", YRef("stmtsep"), Or(YRef("description-stmt"), ""), Or(YRef("revision-date-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), \
    ), YRef("stmtsep")))

YDef("include-stmt", And(YRef("include-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), Or(";", \

    Or(And("{", YRef("stmtsep"), Or(YRef("revision-date-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}"), \
    And("{", YRef("stmtsep"), Or(YRef("revision-date-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(YRef("description-stmt"), ""), "}"), \
    And("{", YRef("stmtsep"), Or(YRef("reference-stmt"), ""), Or(YRef("revision-date-stmt"), ""), Or(YRef("description-stmt"), ""), "}"), \
    And("{", YRef("stmtsep"), Or(YRef("reference-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("revision-date-stmt"), ""), "}"), \
    And("{", YRef("stmtsep"), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(YRef("revision-date-stmt"), ""), "}"), \
    And("{", YRef("stmtsep"), Or(YRef("description-stmt"), ""), Or(YRef("revision-date-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), \
    ), YRef("stmtsep")))

YDef("namespace-stmt", And(YRef("namespace-keyword"), YRef("sep"), YRef("uri-str"), YRef("stmtend")))

YDef("uri-str", String(min=1,max=256))

YDef("prefix-stmt", And(YRef("prefix-keyword"), YRef("sep"), YRef("prefix-arg-str"), YRef("stmtend")))

YDef("belongs-to-stmt", And(YRef("belongs-to-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), "{", YRef("stmtsep"), YRef("prefix-stmt"), "}", YRef("stmtsep")))

YDef("organization-stmt", And(YRef("organization-keyword"), YRef("sep"), YRef("string"), YRef("stmtend")))

YDef("contact-stmt", And(YRef("contact-keyword"), YRef("sep"), YRef("string"), YRef("stmtend")))

YDef("description-stmt", And(YRef("description-keyword"), YRef("sep"), YRef("string"), YRef("stmtend")))

YDef("reference-stmt", And(YRef("reference-keyword"), YRef("sep"), YRef("string"), YRef("stmtend")))

YDef("units-stmt", And(YRef("units-keyword"), YRef("sep"), YRef("string"), YRef("stmtend")))

YDef("revision-stmt", And(YRef("revision-keyword"), YRef("sep"), YRef("revision-date"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(And(Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), "")), And(Or(YRef("reference-stmt"), ""), Or(YRef("description-stmt"), ""))), "}")), YRef("stmtsep")))

YDef("revision-date", YRef("date-arg-str"))

YDef("revision-date-stmt", And(YRef("revision-date-keyword"), YRef("sep"), YRef("revision-date"), YRef("stmtend")))

YDef("extension-stmt", And(YRef("extension-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(YRef("argument-stmt"), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))

YDef("argument-stmt", And(YRef("argument-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), Or(";", And(";", YRef("stmtsep"), Or(YRef("yin-element-stmt"), ""), "}")), YRef("stmtsep")))

YDef("yin-element-stmt", And(YRef("yin-element-keyword"), YRef("sep"), YRef("yin-element-arg-str"), YRef("stmtend")))

YDef("yin-element-arg-str", Or(YRef("true-keyword"), YRef("false-keyword")))

YDef("identity-stmt", And(YRef("identity-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), Or(Join(YRef("base-stmt"), sep="", max=max_repeat), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))

YDef("base-stmt", And(YRef("base-keyword"), YRef("sep"), YRef("identifier-ref-arg-str"), YRef("stmtend")))

YDef("feature-stmt", And(YRef("feature-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))

YDef("if-feature-stmt", And(YRef("if-feature-keyword"), YRef("sep"), YRef("if-feature-expr-str"), YRef("stmtend")))

YDef("if-feature-expr-str", YRef("if-feature-expr"))

YDef("if-feature-expr", And(YRef("if-feature-term"), Or(And(YRef("sep"), YRef("or-keyword"), YRef("sep"), YRef("if-feature-expr")), "")))

YDef("if-feature-term", And(YRef("if-feature-factor"), Or(And(YRef("sep"), YRef("and-keyword"), YRef("sep"), YRef("if-feature-term")), "")))

YDef("if-feature-factor", Or(And(YRef("not-keyword"), YRef("sep"), YRef("if-feature-factor")), And("(", YRef("optsep"), YRef("if-feature-expr"), YRef("optsep"), ")"), YRef("identifier-ref-arg")))

YDef("typedef-stmt", And(YRef("typedef-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), "{", YRef("stmtsep"), YRef("type-stmt"), Or(YRef("units-stmt"), ""), Or(YRef("default-stmt"), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}", YRef("stmtsep")))

YDef("type-stmt", And(YRef("type-keyword"), YRef("sep"), YRef("identifier-ref-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(YRef("type-body-stmts"), ""), "}")), YRef("stmtsep")))

YDef("type-body-stmts", Or(YRef("numerical-restrictions"), YRef("decimal64-specification"), YRef("string-restrictions"), YRef("enum-specification"), YRef("leafref-specification"), YRef("identityref-specification"), YRef("instance-identifier-specification"), YRef("bits-specification"), YRef("union-specification"), YRef("binary-specification")))

YDef("numerical-restrictions", Or(YRef("range-stmt"), ""))

YDef("range-stmt", And(YRef("range-keyword"), YRef("sep"), YRef("range-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(YRef("error-message-stmt"), ""), Or(YRef("error-app-tag-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))

YDef("decimal64-specification", Or(And(YRef("fraction-digits-stmt"), Or(YRef("range-stmt"), "")), And(Or(YRef("range-stmt"), ""), YRef("fraction-digits-stmt"))))

YDef("fraction-digits-stmt", And(YRef("fraction-digits-keyword"), YRef("sep"), YRef("fraction-digits-arg-str"), YRef("stmtend")))

YDef("fraction-digits-arg-str", Or(And("1", Or(Or("0", "1", "2", "3", "4", "5", "6", "7", "8"), "")), "2", "3", "4", "5", "6", "7", "8", "9"))

YDef("string-restrictions", Or(And(Or(YRef("length-stmt"), ""), Or(Join(YRef("pattern-stmt"), sep="", max=max_repeat), "")), And(Or(Join(YRef("pattern-stmt"), sep="", max=max_repeat), ""), Or(YRef("length-stmt"), ""))))

YDef("length-stmt", And(YRef("length-keyword"), YRef("sep"), YRef("length-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(YRef("error-message-stmt"), ""), Or(YRef("error-app-tag-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))

YDef("pattern-stmt", And(YRef("pattern-keyword"), YRef("sep"), YRef("string"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(YRef("modifier-stmt"), ""), Or(YRef("error-message-stmt"), ""), Or(YRef("error-app-tag-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))

YDef("modifier-stmt", And(YRef("modifier-keyword"), YRef("sep"), YRef("modifier-arg-str"), YRef("stmtend")))

YDef("modifier-arg-str", YRef("invert-match-keyword"))

YDef("default-stmt", And(YRef("default-keyword"), YRef("sep"), YRef("string"), YRef("stmtend")))

YDef("enum-specification", Join(YRef("enum-stmt"), sep="", max=max_repeat))

YDef("enum-stmt", And(YRef("enum-keyword"), YRef("sep"), YRef("string"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), Or(YRef("value-stmt"), ""), Or(YRef("error-message-stmt"), ""), Or(YRef("error-app-tag-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))

YDef("leafref-specification", Or(And(YRef("path-stmt"), Or(YRef("require-instance-stmt"), "")), And(Or(YRef("require-instance-stmt"), ""), YRef("path-stmt"))))

YDef("path-stmt", And(YRef("path-keyword"), YRef("sep"), YRef("path-arg-str"), YRef("stmtend")))

YDef("require-instance-stmt", And(YRef("require-instance-keyword"), YRef("sep"), YRef("require-instance-arg"), YRef("stmtend")))

YDef("require-instance-arg-str", YRef("require-instance-arg"))

YDef("require-instance-arg", Or(YRef("true-keyword"), YRef("false-keyword")))

YDef("instance-identifier-specification", Or(YRef("require-instance-stmt"), ""))

YDef("identityref-specification", Join(YRef("base-stmt"), sep="", max=max_repeat))

YDef("union-specification", Join(YRef("type-stmt"), sep="", max=max_repeat))

YDef("binary-specification", Or(YRef("length-stmt"), ""))

YDef("bits-specification", Join(YRef("bit-stmt"), sep="", max=max_repeat))

YDef("bit-stmt", And(YRef("bit-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), Or(YRef("position-stmt"), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))

YDef("position-stmt", And(YRef("position-keyword"), YRef("sep"), YRef("position-value-arg-str"), YRef("stmtend")))

YDef("position-value-arg-str", YRef("non-negative-integer-value"))

YDef("status-stmt", And(YRef("status-keyword"), YRef("sep"), YRef("status-arg-str"), YRef("stmtend")))

YDef("status-arg-str", Or(YRef("current-keyword"), YRef("obsolete-keyword"), YRef("deprecated-keyword")))

YDef("config-stmt", And(YRef("config-keyword"), YRef("sep"), YRef("config-arg-str"), YRef("stmtend")))

YDef("config-arg-str", Or(YRef("true-keyword"), YRef("false-keyword")))

YDef("mandatory-stmt", And(YRef("mandatory-keyword"), YRef("sep"), YRef("mandatory-arg-str"), YRef("stmtend")))

YDef("mandatory-arg-str", Or(YRef("true-keyword"), YRef("false-keyword")))

YDef("presence-stmt", And(YRef("presence-keyword"), YRef("sep"), YRef("string"), YRef("stmtend")))

YDef("ordered-by-stmt", And(YRef("ordered-by-keyword"), YRef("sep"), YRef("ordered-by-arg-str"), YRef("stmtend")))

YDef("ordered-by-arg-str", Or(YRef("user-keyword"), YRef("system-keyword")))

YDef("must-stmt", And(YRef("must-keyword"), YRef("sep"), YRef("string"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(YRef("error-message-stmt"), ""), Or(YRef("error-app-tag-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))

YDef("error-message-stmt", And(YRef("error-message-keyword"), YRef("sep"), YRef("string"), YRef("stmtend")))

YDef("error-app-tag-stmt", And(YRef("error-app-tag-keyword"), YRef("sep"), YRef("string"), YRef("stmtend")))

YDef("min-elements-stmt", And(YRef("min-elements-keyword"), YRef("sep"), YRef("min-value-arg-str"), YRef("stmtend")))

YDef("min-value-arg-str", YRef("non-negative-integer-value"))

YDef("max-elements-stmt", And(YRef("max-elements-keyword"), YRef("sep"), YRef("max-value-arg-str"), YRef("stmtend")))

YDef("max-value-arg-str", Or(YRef("unbounded-keyword"), YRef("positive-integer-value")))

YDef("value-stmt", And(YRef("value-keyword"), YRef("sep"), YRef("integer-value-str"), YRef("stmtend")))

YDef("integer-value-str", Or(And("-", YRef("non-negative-integer-value")), YRef("non-negative-integer-value")))

YDef("grouping-stmt", And(YRef("grouping-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(Join(Or(YRef("typedef-stmt"), YRef("grouping-stmt")), sep="", max=max_repeat), ""), Or(Join(YRef("data-def-stmt"), sep="", max=max_repeat), ""), Or(Join(YRef("action-stmt"), sep="", max=max_repeat), ""), Or(Join(YRef("notification-stmt"), sep="", max=max_repeat), sep="", max=max_repeat), "}")), YRef("stmtsep")))

YDef("container-stmt", And(YRef("container-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), Or(";", And(YRef("stmtsep"), Or(YRef("when-stmt"), ""), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), Or(Join(YRef("must-stmt"), sep="", max=max_repeat), ""), Or(YRef("presence-stmt"), ""), Or(YRef("config-stmt"), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(Join(Or(YRef("typedef-stmt"), YRef("grouping-stmt")), sep="", max=max_repeat), ""), Or(Join(YRef("data-def-stmt"), sep="", max=max_repeat), ""), Or(Join(YRef("action-stmt"), sep="", max=max_repeat), ""), Or(Join(YRef("notification-stmt"), sep="", max=max_repeat), ""), "}")), YRef("stmtsep")))

YDef("leaf-stmt", And(YRef("leaf-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), "{", YRef("stmtsep"), Or(YRef("when-stmt"), ""), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), YRef("type-stmt"), Or(YRef("units-stmt"), ""), Or(Join(YRef("must-stmt"), sep="", max=max_repeat), ""), Or(YRef("default-stmt"), ""), Or(YRef("config-stmt"), ""), Or(YRef("mandatory-stmt"), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}", YRef("stmtsep")))

YDef("leaf-list-stmt", And(YRef("leaf-list-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), "{", YRef("stmtsep"), Or(YRef("when-stmt"), ""), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), YRef("type-stmt"), YRef("stmtsep"), Or(YRef("units-stmt"), ""), Or(Join(YRef("must-stmt"), sep="", max=max_repeat), ""), Or(Join(YRef("default-stmt"), sep="", max=max_repeat), ""), Or(YRef("config-stmt"), ""), Or(YRef("min-elements-stmt"), ""), Or(YRef("max-elements-stmt"), ""), Or(YRef("ordered-by-stmt"), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}", YRef("stmtsep")))

YDef("list-stmt", And(YRef("list-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), "{", YRef("stmtsep"), Or(YRef("when-stmt"), ""), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), Or(Join(YRef("must-stmt"), sep="", max=max_repeat), ""), Or(YRef("key-stmt"), ""), Or(Join(YRef("unique-stmt"), sep="", max=max_repeat), ""), Or(YRef("config-stmt"), ""), Or(YRef("min-elements-stmt"), ""), Or(YRef("max-elements-stmt"), ""), Or(YRef("ordered-by-stmt"), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(Join(Or(YRef("typedef-stmt"), YRef("grouping-stmt")), sep="", max=max_repeat), ""), Join(YRef("data-def-stmt"), sep="", max=max_repeat), Or(Join(YRef("action-stmt"), sep="", max=max_repeat), ""), Or(Join(YRef("notification-stmt"), sep="", max=max_repeat), ""), "}", YRef("stmtsep")))

YDef("key-stmt", And(YRef("key-keyword"), YRef("sep"), YRef("key-arg-str"), YRef("stmtend")))

YDef("key-arg-str", YRef("key-arg"))

YDef("key-arg", And(YRef("node-identifier"), Or(Join(And(YRef("sep"), YRef("node-identifier")), sep="", max=max_repeat), "")))

YDef("unique-stmt", And(YRef("unique-keyword"), YRef("sep"), YRef("unique-arg-str"), YRef("stmtend")))

YDef("unique-arg-str", YRef("unique-arg"))

YDef("unique-arg", And(YRef("descendant-schema-nodeid"), Or(Join(And(YRef("sep"), YRef("descendant-schema-nodeid")), sep="", max=max_repeat), "")))

YDef("choice-stmt", And(YRef("choice-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(YRef("when-stmt"), ""), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), Or(YRef("default-stmt"), ""), Or(YRef("config-stmt"), ""), Or(YRef("mandatory-stmt"), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(Join(Or(YRef("short-case-stmt"), YRef("case-stmt")), sep="", max=max_repeat), ""), "}")), YRef("stmtsep")))

YDef("short-case-stmt", Or(YRef("choice-stmt"), YRef("container-stmt"), YRef("leaf-stmt"), YRef("leaf-list-stmt"), YRef("list-stmt"), YRef("list-stmt"), YRef("anydata-stmt"), YRef("anyxml-stmt")))

YDef("case-stmt", And(YRef("case-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(YRef("when-stmt"), ""), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(Join(YRef("data-def-stmt"), sep="", max=max_repeat), ""), "}")), YRef("stmtsep")))

YDef("anydata-stmt", And(YRef("anydata-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(YRef("when-stmt"), ""), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), Or(Join(YRef("must-stmt"), sep="", max=max_repeat), ""), Or(YRef("config-stmt"), ""), Or(YRef("mandatory-stmt"), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))

YDef("anyxml-stmt", And(YRef("anydata-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(YRef("when-stmt"), ""), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), Or(Join(YRef("must-stmt"), sep="", max=max_repeat), ""), Or(YRef("config-stmt"), ""), Or(YRef("mandatory-stmt"), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))

YDef("uses-stmt", And(YRef("uses-keyword"), YRef("sep"), YRef("identifier-ref-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(YRef("when-stmt"), ""), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(Join(YRef("refine-stmt"), sep="", max=max_repeat), ""), Or(Join(YRef("uses-augment-stmt"), sep="", max=max_repeat), ""), "}")), YRef("stmtsep")))

YDef("refine-stmt", And(YRef("refine-keyword"), YRef("sep"), YRef("refine-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), Or(Join(YRef("must-stmt"), sep="", max=max_repeat), ""), Or(YRef("presence-stmt"), ""), Or(Join(YRef("default-stmt"), sep="", max=max_repeat), ""), Or(YRef("config-stmt"), ""), Or(YRef("mandatory-stmt"), ""), Or(YRef("min-elements-stmt"), ""), Or(YRef("max-elements-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))

YDef("refine-arg-str", YRef("refine-arg"))

YDef("refine-arg", YRef("descendant-schema-nodeid"))

YDef("uses-augment-stmt", And(YRef("augment-keyword"), YRef("sep"), YRef("uses-augment-arg-str"), YRef("optsep"), "{", YRef("stmtsep"), Or(YRef("when-stmt"), ""), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), Join(Or(YRef("data-def-stmt"), YRef("case-stmt"), YRef("action-stmt"), YRef("notification-stmt")), sep="", max=max_repeat), "}"), YRef("stmtsep"))

YDef("uses-augment-arg-str", YRef("uses-augment-arg"))

YDef("uses-augment-arg", YRef("descendant-schema-nodeid"))

YDef("augment-stmt", And(YRef("augment-keyword"), YRef("sep"), YRef("augment-arg-str"), YRef("optsep"), "{", YRef("stmtsep"), Or(YRef("when-stmt"), ""), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), Join(Or(YRef("data-def-stmt"), YRef("case-stmt"), YRef("action-stmt"), YRef("notification-stmt")), sep="", max=max_repeat), "}", YRef("stmtsep")))

YDef("augment-arg-str", YRef("augment-arg"))

YDef("augment-arg", YRef("absolute-schema-nodeid"))

YDef("when-stmt", And(YRef("when-keyword"), YRef("sep"), YRef("string"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), "}")), YRef("stmtsep")))

YDef("rpc-stmt", And(YRef("rpc-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(Join(Or(YRef("typedef-stmt"), YRef("grouping-stmt")), sep="", max=max_repeat), ""), Or(YRef("input-stmt"), ""), Or(YRef("output-stmt"), ""), "}")), YRef("stmtsep")))

YDef("action-stmt", And(YRef("action-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(Join(Or(YRef("typedef-stmt"), YRef("grouping-stmt")), sep="", max=max_repeat), ""), Or(YRef("input-stmt"), ""), Or(YRef("output-stmt"), ""), "}")), YRef("stmtsep")))

YDef("input-stmt", And(YRef("input-keyword"), YRef("optsep"), "{", YRef("stmtsep"), Or(Join(YRef("must-stmt"), sep="", max=max_repeat), ""), Or(Join(Or(YRef("typedef-stmt"), YRef("grouping-stmt")), sep="", max=max_repeat), ""), Join(YRef("data-def-stmt"), sep="", max=max_repeat), "}", YRef("stmtsep")))

YDef("output-stmt", And(YRef("output-keyword"), YRef("optsep"), "{", YRef("stmtsep"), Or(Join(YRef("must-stmt"), sep="", max=max_repeat), ""), Or(Join(Or(YRef("typedef-stmt"), YRef("grouping-stmt")), sep="", max=max_repeat), ""), Join(YRef("data-def-stmt"), sep="", max=max_repeat), "}", YRef("stmtsep")))

YDef("notification-stmt", And(YRef("notification-keyword"), YRef("sep"), YRef("identifier-arg-str"), YRef("optsep"), Or(";", And("{", YRef("stmtsep"), Or(Join(YRef("if-feature-stmt"), sep="", max=max_repeat), ""), Or(Join(YRef("must-stmt"), sep="", max=max_repeat), ""), Or(YRef("status-stmt"), ""), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(Join(Or(YRef("typedef-stmt"), YRef("grouping-stmt")), sep="", max=max_repeat), ""), Join(YRef("data-def-stmt"), sep="", max=max_repeat), "}")), YRef("stmtsep")))

YDef("deviation-stmt", And(YRef("deviation-keyword"), YRef("sep"), YRef("deviation-arg-str"), YRef("optsep"), "{", YRef("stmtsep"), Or(YRef("description-stmt"), ""), Or(YRef("reference-stmt"), ""), Or(YRef("deviate-not-supported-stmt"), Join(Or(YRef("deviate-add-stmt"), YRef("deviate-replace-stmt"), YRef("deviate-delete-stmt")), sep="", max=max_repeat), "}", YRef("stmtsep"))))

YDef("deviation-arg-str", YRef("deviation-arg"))

YDef("deviation-arg", YRef("absolute-schema-nodeid"))

YDef("deviate-not-supported-stmt", And(YRef("deviate-keyword"), YRef("sep"), YRef("not-supported-keyword-str"), YRef("stmtend")))

YDef("deviate-add-stmt", And(YRef("deviate-keyword"), YRef("sep"), YRef("add-keyword-str"), YRef("optsep"), Or(";", And(YRef("stmtsep"), Or(YRef("units-stmt"), ""), Or(Join(YRef("must-stmt"), sep="", max=max_repeat), ""), Or(Join(YRef("unique-stmt"), sep="", max=max_repeat), ""), Or(Join(YRef("default-stmt"), sep="", max=max_repeat), ""), Or(YRef("config-stmt"), ""), Or(YRef("mandatory-stmt"), ""), Or(YRef("min-elements-stmt"), ""), Or(YRef("max-elements-stmt"), ""), "}")), YRef("stmtsep")))

YDef("deviate-delete-stmt", And(YRef("deviate-keyword"), YRef("sep"), YRef("delete-keyword-str"), YRef("optsep"), Or(";", And(YRef("stmtsep"), Or(YRef("units-stmt"), ""), Or(Join(YRef("must-stmt"), sep="", max=max_repeat), ""), Or(Join(YRef("unique-stmt"), sep="", max=max_repeat), ""), Or(Join(YRef("default-stmt"), sep="", max=max_repeat), ""), Or(YRef("config-stmt"), ""), Or(YRef("mandatory-stmt"), ""), Or(YRef("min-elements-stmt"), ""), Or(YRef("max-elements-stmt"), ""), "}")), YRef("stmtsep")))

YDef("deviate-replace-stmt", And(YRef("deviate-keyword"), YRef("sep"), YRef("replace-keyword-str"), YRef("optsep"), Or(";", And(YRef("stmtsep"), Or(YRef("type-stmt"), ""), Or(YRef("units-stmt"), ""), Or(YRef("default-stmt"), ""), Or(YRef("config-stmt"), ""), Or(YRef("mandatory-stmt"), ""), Or(YRef("min-elements-stmt"), ""), Or(YRef("max-elements-stmt"), ""), "}")), YRef("stmtsep")))

YDef("not-supported-keyword-str", YRef("not-supported-keyword"))

YDef("add-keyword-str", YRef("add-keyword"))

YDef("delete-keyword-str", YRef("delete-keyword"))

YDef("replace-keyword-str", YRef("replace-keyword"))

YDef("unknown-statement", And(YRef("prefix"), ":", YRef("identifier"), Or(And(YRef("sep"), YRef("string")), ""), YRef("optsep"), Or(";", And("{", YRef("optsep"), Or(Join(And(Or(YRef("yang-stmt"), YRef("unknown-statement")), YRef("optsep")), sep="", max=max_repeat), "}")), YRef("stmtsep"))))

YDef("yang-stmt", Or(YRef("action-stmt"), YRef("anydata-stmt"), YRef("anyxml-stmt"), YRef("argument-stmt"), YRef("augment-stmt"), YRef("base-stmt"), YRef("belongs-to-stmt"), YRef("bit-stmt"), YRef("case-stmt"), YRef("choice-stmt"), YRef("config-stmt"), YRef("contact-stmt"), YRef("container-stmt"), YRef("default-stmt"), YRef("description-stmt"), YRef("deviate-add-stmt"), YRef("deviate-delete-stmt"), YRef("deviate-not-supported-stmt"), YRef("deviate-replace-stmt"), YRef("deviation-stmt"), YRef("enum-stmt"), YRef("error-app-tag-stmt"), YRef("error-message-stmt"), YRef("extension-stmt"), YRef("feature-stmt"), YRef("fraction-digits-stmt"), YRef("grouping-stmt"), YRef("identity-stmt"), YRef("if-feature-stmt"), YRef("import-stmt"), YRef("include-stmt"), YRef("input-stmt"), YRef("key-stmt"), YRef("leaf-list-stmt"), YRef("leaf-stmt"), YRef("length-stmt"), YRef("list-stmt"), YRef("mandatory-stmt"), YRef("max-elements-stmt"), YRef("min-elements-stmt"), YRef("modifier-stmt"), YRef("module-stmt"), YRef("must-stmt"), YRef("namespace-stmt"), YRef("notification-stmt"), YRef("ordered-by-stmt"), YRef("organization-stmt"), YRef("output-stmt"), YRef("path-stmt"), YRef("pattern-stmt"), YRef("position-stmt"), YRef("prefix-stmt"), YRef("presence-stmt"), YRef("range-stmt"), YRef("reference-stmt"), YRef("refine-stmt"), YRef("require-instance-stmt"), YRef("revision-date-stmt"), YRef("revision-stmt"), YRef("rpc-stmt"), YRef("status-stmt"), YRef("submodule-stmt"), YRef("typedef-stmt"), YRef("type-stmt"), YRef("unique-stmt"), YRef("units-stmt"), YRef("uses-augment-stmt"), YRef("uses-stmt"), YRef("value-stmt"), YRef("when-stmt"), YRef("yang-version-stmt"), YRef("yin-element-stmt")))


YDef("range-arg-str", YRef("range-arg"))

YDef("range-arg", And(YRef("range-part"), Or(Join(And(YRef("optsep"), "|", YRef("optsep"), YRef("range-part")), sep="", max=max_repeat), "")))

YDef("range-part", And(YRef("range-boundary"), Or(And(YRef("optsep"), "..", YRef("optsep"), YRef("range-boundary")), "")))

YDef("range-boundary", Or(YRef("min-keyword"), YRef("max-keyword"), YRef("decimal-value")))

YDef("length-arg-str", YRef("length-arg"))

YDef("length-arg", And(YRef("length-part"), Or(Join(And(YRef("optsep"), "|", YRef("optsep"), YRef("length-part")), sep="", max=max_repeat), "")))

YDef("length-part", And(YRef("length-boundary"), Or(And(YRef("optsep"), "..", YRef("optsep"), YRef("length-boundary")), "")))

YDef("length-boundary", Or(YRef("min-keyword"), YRef("max-keyword"), YRef("non-negative-integer-value")))

YDef("date-arg-str", YRef("date-arg"))

YDef("date-arg", And(YRef("DIGIT"), YRef("DIGIT"), YRef("DIGIT"), YRef("DIGIT"), "-", YRef("DIGIT"), YRef("DIGIT"), "-", YRef("DIGIT"), YRef("DIGIT")))

YDef("schema-nodeid", Or(YRef("absolute-schema-nodeid"), YRef("descendant-schema-nodeid")))

YDef("absolute-schema-nodeid", Join(And("/", YRef("node-identifier")), sep="", max=max_repeat))

YDef("descendant-schema-nodeid", And(YRef("node-identifier"), Or(YRef("absolute-schema-nodeid"), "")))

YDef("node-identifier", And(Or(And(YRef("prefix"), ":"), ""), YRef("identifier")))

YDef("instance-identifier", Join(And("/", And(YRef("node-identifier"), Or(Or(Join(YRef("key-predicate"), sep="", max=max_repeat), YRef("leaf-list-predicate"), YRef("pos")), ""))), sep="", max=max_repeat))

YDef("key-predicate", And("[", Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), YRef("key-predicate-expr"), Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), "]"))

YDef("key-predicate-expr", And(YRef("node-identifier"), Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), "="), Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), YRef("quoted-string"))

YDef("leaf-list-predicate", And("[", Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), YRef("leaf-list-predicate-expr"), Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), "]"))

YDef("leaf-list-predicate-expr", And(".", Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), "=", Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), YRef("quoted-string")))

YDef("pos", And("[", Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), YRef("positive-integer-value"), Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), "]"))

YDef("quoted-string", Or(And(YRef("DQUOTE"), YRef("string"), YRef("DQUOTE")), And(YRef("SQUOTE"), YRef("string"), YRef("SQUOTE"))))

YDef("path-arg-str", YRef("path-arg"))

YDef("path-arg", Or(YRef("absolute-path"), YRef("relative-path")))

YDef("absolute-path", Join(And("/", YRef("node-identifier"), Or(Join(YRef("path-predicate"), sep="", max=max_repeat), "")), sep="", max=max_repeat))

YDef("relative-path", And(Join("../", sep="", max=max_repeat), YRef("descendant-path")))

YDef("descendant-path", And(YRef("node-identifier"), Or(And(Or(Join(YRef("path-predicate"), sep="", max=max_repeat), ""), YRef("absolute-path")), "")))

YDef("path-predicate", And("[", Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), "=", YRef("path-equality-expr"), Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), "]"))

YDef("path-equality-expr", And(YRef("node-identifier"), Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), "=", Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), YRef("path-key-expr")))

YDef("path-key-expr", And(YRef("current-function-invocation"), Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), "/", Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), YRef("rel-path-keyexpr")))

YDef("rel-path-keyexpr", And(Join(And(".." ,Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), "/", Or(Join(YRef("WSP"), sep="", max=max_repeat), "")), sep="", max=max_repeat), Or(Join(And(YRef("node-identifier"), Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), "/", Or(Join(YRef("WSP"), sep="", max=max_repeat), "")), sep="", max=max_repeat), ""), YRef("node-identifier")))

YDef("action-keyword", "action")

YDef("anydata-keyword", "anydata")

YDef("anyxml-keyword", "anyxml")

YDef("argument-keyword", "argument")

YDef("augment-keyword", "augment")

YDef("base-keyword", "base")

YDef("belongs-to-keyword", "belongs-to")

YDef("bit-keyword", "bit")

YDef("case-keyword", "case")

YDef("choice-keyword", "choice")

YDef("config-keyword", "config")

YDef("contact-keyword", "contact")

YDef("container-keyword", "container")

YDef("default-keyword", "default")

YDef("description-keyword", "description")

YDef("deviate-keyword", "deviate")

YDef("deviation-keyword", "deviation")

YDef("enum-keyword", "enum")

YDef("error-app-tag-keyword", "error-app-tag")

YDef("error-message-keyword", "error-message")

YDef("extension-keyword", "extension")

YDef("feature-keyword", "feature")

YDef("fraction-digits-keyword", "fraction-digits")

YDef("grouping-keyword", "grouping")

YDef("identity-keyword", "identity")

YDef("if-feature-keyword", "if-feature")

YDef("import-keyword", "import")

YDef("include-keyword", "include")

YDef("input-keyword", "input")

YDef("key-keyword", "key")

YDef("leaf-keyword", "leaf")

YDef("leaf-list-keyword", "leaf-list")

YDef("length-keyword", "length")

YDef("list-keyword", "list")

YDef("mandatory-keyword", "mandatory")

YDef("max-elements-keyword", "max-elements")

YDef("min-elements-keyword", "min-elements")

YDef("modifier-keyword", "modifier")

YDef("module-keyword", "module")

YDef("must-keyword", "must")

YDef("namespace-keyword", "namespace")

YDef("notification-keyword", "notification")

YDef("ordered-by-keyword", "ordered-by")

YDef("organization-keyword", "organization")

YDef("output-keyword", "output")

YDef("path-keyword", "path")

YDef("pattern-keyword", "pattern")

YDef("position-keyword", "position")

YDef("prefix-keyword", "prefix")

YDef("presence-keyword", "presence")

YDef("range-keyword", "range")

YDef("reference-keyword", "reference")

YDef("refine-keyword", "refine")

YDef("require-instance-keyword", "require-instance")

YDef("revision-keyword", "revision")

YDef("revision-date-keyword", "revision-date")

YDef("rpc-keyword", "rpc")

YDef("status-keyword", "status")

YDef("submodule-keyword", "submodule")

YDef("type-keyword", "type")

YDef("typedef-keyword", "typedef")

YDef("unique-keyword", "unique")

YDef("units-keyword", "units")

YDef("uses-keyword", "uses")

YDef("value-keyword", "value")

YDef("when-keyword", "when")

YDef("yang-version-keyword", "yang-version")

YDef("yin-element-keyword", "yin-element")

YDef("add-keyword", "add")

YDef("current-keyword", "current")

YDef("delete-keyword", "deleted")

YDef("deprecated-keyword", "deprecated")

YDef("false-keyword", "false")

YDef("invert-match-keyword", "invert-match")

YDef("max-keyword", "max")

YDef("min-keyword", "min")

YDef("not-supported-keyword", "not-supported")

YDef("obsolete-keyword", "obsolete")

YDef("replace-keyword", "replace")

YDef("system-keyword", "system")

YDef("true-keyword", "true")

YDef("unbounded-keyword", "unbounded")

YDef("user-keyword", "user")

YDef("and-keyword", "and")

YDef("or-keyword", "or")

YDef("not-keyword", "not")

YDef("current-function-invocation", And(YRef("current-keyword"), Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), "(", Or(Join(YRef("WSP"), sep="", max=max_repeat), ""), ")"))

YDef("prefix-arg-str", YRef("prefix-arg"))

YDef("prefix-arg", YRef("prefix"))

YDef("prefix", YRef("identifier"))

YDef("identifier-arg-str", YRef("identifier-arg"))

YDef("identifier-arg", YRef("identifier"))

YDef("identifier", And(Or(YRef("ALPHA"), "_"), Or(Join(Or(YRef("ALPHA"), YRef("DIGIT"), "_", "-", "."), sep="", max=max_repeat), "")))

YDef("identifier-ref-arg-str", YRef("identifier-ref-arg"))

YDef("identifier-ref-arg", YRef("identifier-ref"))

YDef("identifier-ref", And(Or(And(YRef("prefix"), ":"), ""), YRef("identifier")))

YDef("string", YRef("yang-string"))

YDef("yang-string", Or(Join(YRef("yang-char"), sep="", max=max_repeat), ""))

YDef("yang-char", String(max=1))

YDef("integer-value", Or(And("-", YRef("non-negative-integer-value")), YRef("non-negative-integer-value")))

YDef("non-negative-integer-value", Or("0", YRef("positive-integer-value")))

YDef("positive-integer-value", And(YRef("non-zero-digit"), Or(Join(YRef("DIGIT"), sep="", max=max_repeat), "")))

YDef("zero-integer-value", Join(YRef("DIGIT"), sep="", max=max_repeat))

YDef("stmtend", And(YRef("optsep"), Or(";", And("{", YRef("stmtsep"), "}")), YRef("stmtsep")))

YDef("sep", Join(Or(YRef("WSP"), YRef("line-break")), sep="", max=max_repeat))

YDef("optsep", Or(Join(Or(YRef("WSP"), YRef("line-break")), sep="", max=max_repeat), ""))

YDef("stmtsep", Or(Join(Or(YRef("WSP"), YRef("line-break"), YRef("unknown-statement")), sep="", max=max_repeat), ""))

YDef("line-break", Or(YRef("CRLF"), YRef("LF")))

YDef("non-zero-digit", String(charset="123456789"))

YDef("decimal-value", And(YRef("integer-value"), ".", YRef("zero-integer-value")))

YDef("SQUOTE", "'")

YDef("ALPHA", String(charset=String.charset_alpha))

YDef("CR", "")

YDef("CRLF", And(YRef("CR"), YRef("LF")))

YDef("DIGIT", String(charset="0123456789"))

YDef("DQUOTE", "\"")

YDef("HTAB", "\t")

YDef("LF", "\n")

YDef("SP", " ")

YDef("WSP", Or(YRef("SP"), YRef("HTAB")))
