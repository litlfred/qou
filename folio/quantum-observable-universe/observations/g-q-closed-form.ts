import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:gravity-spectral-prefactor",
  label: "rem:g-q-closed-form",
  title:
    "Closed $q$-rational form of $G(q)$ and Planck-unit consistency",
  uses: [
    "prop:gravity-spectral-prefactor",
    "def:gravitational-constant",
    "rem:regime-table",
  ],
  tags: [
    "gravity",
    "newton-constant",
    "planck-units",
    "q-rational",
    "closed-form",
    "information-theory",
  ],
});
