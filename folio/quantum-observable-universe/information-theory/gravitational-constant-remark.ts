import { remark } from "../../schema/builders";

export default remark({
  label: "rem:gravitational-constant-remark",
  title: "Role of the gravitational constant in the field equation",
  interprets: "def:gravitational-constant",
  tags: ["definition-commentary"],
  uses: [
    "def:gravitational-constant",
    "def:q-yang-mills-levi",
    "rem:gr-substrate-geometry",
  ],
});
