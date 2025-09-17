----------------------------
Trustable Compliance Report
----------------------------



Item status guide 
#################
Each item in a Trustable Graph is scored with a number between 0 and 1.
The score represents aggregated organizational confidence in a given Statement, with larger numbers corresponding to higher confidence.

The status of an item and its links also affect the score.

Unreviewed items are indicated by a strikethrough.
The score of unreviewed items is always set to zero.


Suspect links are indicated by italics.
The contribution to the score of a parent item by a suspiciously linked child is always zero, regardless of the child's own score.

Compliance for AOU
##################
This presents the compliance for the Assumptions of Use (AOU) in tabular form.

.. needtable::
   :types: aou_req
   :columns: title as "Item";id as "Item link";content as "Summary"; Score
   :style: table

Compliance for JLEX
####################
This presents the compliance for the JSON-Library Expectations (JLEX) in tabular form.

.. needtable::
   :types: TSF
   :filter: "JLEX" in title
   :columns: title as "Item";id as "Item link";content as "Summary"; Score
   :style: table


Compliance for WFJ
####################
This presents the compliance for the Well Formed JSON (WFJ) in tabular form.

.. needtable::
   :types: TSF
   :filter: "WFJ" in title
   :columns: title as "Item";id as "Item link";content as "Summary"; Score
   :style: table
