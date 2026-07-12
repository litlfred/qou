import { remark } from "../../schema/builders";

export default remark({
  label: "rem:categorical-sha-local-global",
  title: "The $q$-Tate--Shafarevich group as the local-global obstruction",
  interprets: "def:categorical-mordell-weil",
  tags: [
    "birch-swinnerton-dyer",
    "tate-shafarevich",
    "local-global",
    "categorical",
  ],
  uses: [
    "def:categorical-mordell-weil",
  ],
});
