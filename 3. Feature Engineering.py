# Add feature: byte_ratio
df['byte_ratio'] = df['sbytes'] / (df['dbytes'] + 1)

# Add feature: is_common_port (based on ct_dst_sport_ltm which can hint at dest port)
df['is_common_port'] = df['ct_dst_sport_ltm'].isin([80, 443, 22]).astype(int)

# Add feature: flow_intensity = (spkts + dpkts) / dur
df['flow_intensity'] = (df['spkts'] + df['dpkts']) / (df['dur'] + 1e-6)