# Distributed AI Inference Cluster Manager

Orquestrador para distribuir inferência de modelos pesados entre múltiplos nós (ex.: dual-socket Xeon). Balanceia requisições para otimizar temperatura e uso de CPU/GPU.

## Stack

- Kubernetes
- Python FastAPI (gateway)
- Bash (bootstrap)
- Grafana + Prometheus

## Topologia de rede

```
                    ┌─────────────────┐
 Clients ─────────► │  API Gateway    │
                    │  (FastAPI)      │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌──────────┐  ┌──────────┐  ┌──────────┐
        │ Worker 1 │  │ Worker 2 │  │ Worker N │
        │ GPU/CPU  │  │ GPU/CPU  │  │ GPU/CPU  │
        └──────────┘  └──────────┘  └──────────┘
```

Documentação: [docs/TOPOLOGY.md](docs/TOPOLOGY.md)

## Bootstrap de novos nós

```bash
./scripts/bootstrap/join-node.sh --master https://cluster.example --token <TOKEN>
```

O script instala: containerd, nvidia-container-toolkit, node exporter, agente de inferência.

## Monitoramento Grafana

- Dashboard pré-provisionado: `monitoring/grafana/dashboards/inference.json`
- Métricas: latência p99, tokens/s, GPU util, temperatura, fila de requisições.

```bash
kubectl apply -f k8s/
# Acesse Grafana via port-forward
kubectl port-forward svc/grafana 3000:3000
```

## Balanceamento

- **Round-robin** com health check HTTP `/health`.
- **Least-queue**: roteia para worker com menor fila.
- **Thermal-aware** (opcional): reduz carga em nós acima de 80°C.

## Estrutura

| Pasta | Conteúdo |
|-------|----------|
| `k8s/` | Deployments, Services, HPA |
| `api/` | Gateway FastAPI |
| `scripts/bootstrap/` | Join e init |
| `monitoring/` | Prometheus rules, Grafana |
