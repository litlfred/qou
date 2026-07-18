import { remark } from "../../schema/builders";

export default remark({
  interprets: "prop:vorticity-lower-bound",
  label: "rem:vorticity-lower-bound-argument",
  title: "Biot--Savart dynamics and vorticity concentration behind the lower bound",
  uses: ["prop:vorticity-lower-bound"],
  tags: ["vorticity", "biot-savart", "anti-parallel", "interpretation"],
});
