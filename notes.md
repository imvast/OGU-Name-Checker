<h2>Username Checker</h2>

**POST** https://ogu.gg/xmlhttp.php?action=username_availability

**Payload:**

    "username":    "*username*",
    "my_post_key": "b9dce352f5fa2226533172975fa706e5"

<h2>Gen</h2>

**POST** https://ogu.gg/member.php

**Payload:**

    allownotices:         "1",
    recievepms:           "1",
    pmnotice:             "1",
    regcheck1:            "",
    regcheck2:            "true",
    username:             "*username*",
    password:             "*password*",
    email:                "*email*", // gen from any tempmail
    g-recaptcha-response: "*g-recaptcha-response*",
    regtime:              "*timestamp*",
    step:                 "registration",
    action:               "do_register",
    regsubmit:            "Submit Registration",