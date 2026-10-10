import { remark } from "../../schema/builders";

export default remark({
  label: "rem:lqg-adm-ashtekar-comparison",
  title:
    "QOU as the categorical resolution of ADM, Ashtekar, and Smolin--Rovelli",
  tags: [
    "loop-quantum-gravity",
    "adm",
    "ashtekar",
    "spin-network",
    "spin-foam",
    "kodama-state",
    "wheeler-dewitt",
    "barbero-immirzi",
    "comparison",
  ],
  uses: [
    "def:categorical-dirac-operator",
    "def:categorical-instanton",
    "prop:reeb-u1-chart-swap",
    "def:contact-affine-chart",
    "thm:categorical-reeb-exists",
    "ex:categorical-reeb-brings",
    "def:frobenius-hopf-substrate",
    "def:adelic-substrate",
    "rem:yang-mills-surreal-bound",
    "conj:os-reflection-positivity-from-reeb",
  ],
  cites: [
    "ashtekar1986",
    "rovelli1995",
    "rovelli2004",
    "thiemann2007",
  ],
  interprets: "def:categorical-dirac-operator",
});
