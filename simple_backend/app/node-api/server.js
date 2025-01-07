const express = require('express');
const axios = require('axios');

const app = express();
app.use(express.json());

// Frontend -> Node API
app.post('/api/calculate', async (req, res) => {
  const { a, b } = req.body;

  try {
    // Node -> FastAPI Backend
    const response = await axios.post('http://fastapi-service:8000/calculate', { a, b });
    res.json({ result: response.data.result });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

const PORT = 3000;
app.listen(PORT, () => console.log(`Node API running on port ${PORT}`));
