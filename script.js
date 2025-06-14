async function generateVideo() {
  const prompt = document.getElementById('promptInput').value.trim();
  const video = document.getElementById('videoPlayer');
  const loading = document.getElementById('loading');

  if (!prompt) {
    alert("Please enter a Bible story prompt.");
    return;
  }

  loading.style.display = 'block';
  video.style.display = 'none';

  try {
    const response = await fetch("https://api.replicate.com/v1/predictions", {
      method: "POST",
      headers: {
        "Authorization": "   ",
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        version: "b8d7315c-9fdb-4f1c-a4fa-b54d92f8f5de",  // Zeroscope version ID
        input: {
          prompt: prompt,
          guidance_scale: 15,
          num_inference_steps: 25
        }
      })
    });

    const prediction = await response.json();
    const statusUrl = prediction.urls.get;

    let output = null;
    while (!output) {
      const statusResp = await fetch(statusUrl, {
        headers: { "Authorization": "    " }
      });
      const statusJson = await statusResp.json();
      if (statusJson.status === "succeeded") {
        output = statusJson.output;
      } else if (statusJson.status === "failed") {
        throw new Error("Video generation failed.");
      }
      await new Promise(r => setTimeout(r, 3000));
    }

    video.src = output[0];
    video.style.display = 'block';
    loading.style.display = 'none';

  } catch (err) {
    console.error(err);
    alert("Something went wrong. Check console or API token.");
    loading.style.display = 'none';
  }
}
