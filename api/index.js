export default function handler(request, response) {
  const html = `
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>WorkWithIsland Analysis</title>
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  </head>
  <body>
      <div class="container mt-5">
          <div class="row">
              <div class="col-12 text-center">
                  <h1>WorkWithIsland Analysis Dashboard</h1>
                  <div class="alert alert-success mt-4">
                      Server is working! (JavaScript Edge Function)
                  </div>
                  <p class="mt-4">
                      This is a minimal version of the dashboard using JavaScript Edge Function.
                  </p>
                  <div class="mt-4">
                      <h3>Statistics</h3>
                      <p>Total France Questions: 100+</p>
                      <p>Total Countries Questions: 200+</p>
                      <p>Total Personas Questions: 50+</p>
                  </div>
              </div>
          </div>
      </div>
      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
  </body>
  </html>
  `;
  
  return new Response(html, {
    status: 200,
    headers: {
      'Content-Type': 'text/html'
    }
  });
} 