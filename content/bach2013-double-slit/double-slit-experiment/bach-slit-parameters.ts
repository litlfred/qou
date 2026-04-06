import { remark } from "../../schema/builders";

export default remark({
  label: "rem:bach-slit-parameters",
  title: "Slit Geometry (Bach et al. 2013)",
  uses: ["rem:bach-apparatus"],
  tags: ["imported", "arxiv:1210.6243", "double-slit", "experimental"],
  meta: {
    source: "arxiv:1210.6243",
    originalSection: "2",
    importedAt: "2026-03-25T00:00:00Z",
  },
});
