# Topologia de rede

## VLANs recomendadas

| VLAN | Uso |
|------|-----|
| 10 | API pública (LB) |
| 20 | Workers (sem internet direta) |
| 30 | Storage (NFS / object store) |

## Portas

| Serviço | Porta |
|---------|-------|
| Gateway | 443 |
| Worker inference | 8001 |
| Prometheus | 9090 |
| Grafana | 3000 |

## HA

- Mínimo 2 replicas do gateway atrás de Ingress.
- Workers com PodDisruptionBudget `minAvailable: 1`.
