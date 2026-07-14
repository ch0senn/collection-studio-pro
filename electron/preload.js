const { contextBridge } = require("electron");

contextBridge.exposeInMainWorld("collectionStudio", {
    version: "0.3.0"
});
