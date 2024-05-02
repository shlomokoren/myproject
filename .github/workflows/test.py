versions = ['9.9.5-enterprise', '9.9-enterprise', '10.5.1-enterprise', '10.5-enterprise', '9.9.4-enterprise', '10.5.0-enterprise', '10.4.1-enterprise', '10.4-enterprise', '10.4.0-enterprise', '9.9.3-enterprise', '10.3.0-enterprise', '10.3-enterprise', '10.2.1-enterprise', '10.2-enterprise', '9.9.2-enterprise', '9.9.1-enterprise', '10.2.0-enterprise', '10.1.0-enterprise', '10.1-enterprise', '10.0.0-enterprise', '10.0-enterprise', '9.9.0-enterprise', '9.8.0-enterprise', '9.8-enterprise', '8.9.10-enterprise', '8.9-enterprise', '9.7.1-enterprise', '9.7-enterprise', '9.7.0-enterprise', '9.6.1-enterprise', '9.6-enterprise', '8.9.9-enterprise', '9.6.0-enterprise', '9.5-enterprise', '9.5.0-enterprise']
#versions = ['9.9.5-enterprise', '9.9-enterprise', '10.5.1-enterprise']
#versions = ['9.9.5', '9.9', '10.5.1']
sorted_versions = sorted(versions, key=lambda x: [int(num) if num.isdigit() else num for num in x.split('-')[0].split('.')])

print(sorted_versions)
print(sorted_versions[-1])
