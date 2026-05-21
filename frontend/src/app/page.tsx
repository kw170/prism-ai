"use client";

import { useState } from "react";

export default function Home() {
  const [prUrl, setPrUrl] = useState("");
  const [logs, setLogs] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);

  async function handleAnalyze() {
    setLoading(true);
    setResult(null);

    try {
      const res = await fetch("http://localhost:8000/report", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          //diff: prUrl, // temporarily using PR URL as diff input
          pr_url: prUrl,
          logs: logs || "",
        }),
      });

      const data = await res.json();
      setResult(data);
    } catch (err) {
      setResult({ error: "Failed to connect to backend" });
    }

    setLoading(false);
  }

  return (
    <main className="p-10 max-w-3xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">
        🧠 PR Detective
      </h1>

      <div className="space-y-4">
        <input
          className="w-full border p-3 rounded"
          placeholder="Paste PR URL or diff"
          value={prUrl}
          onChange={(e) => setPrUrl(e.target.value)}
        />

        <textarea
          className="w-full border p-3 rounded h-32"
          placeholder="Optional: CI logs"
          value={logs}
          onChange={(e) => setLogs(e.target.value)}
        />

        <button
          onClick={handleAnalyze}
          className="bg-black text-white px-4 py-2 rounded"
        >
          {loading ? "Analyzing..." : "Analyze PR"}
        </button>
      </div>

      {result && (
        <div className="mt-8 p-4 border rounded">
          <h2 className="font-bold mb-2">Result</h2>
          <pre className="text-sm whitespace-pre-wrap">
            {JSON.stringify(result, null, 2)}
          </pre>
        </div>
      )}
    </main>
  );
}