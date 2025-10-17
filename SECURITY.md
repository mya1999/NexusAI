# Security Policy

## Supported Versions

We release patches for security vulnerabilities for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability, please send an email to security@nexusai.com with:

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

We will respond within 48 hours and work with you to resolve the issue.

## Security Best Practices

### For Deployment

1. **Change Default Credentials**: Always change the default SECRET_KEY and database credentials
2. **Use HTTPS**: Deploy behind a reverse proxy with SSL/TLS
3. **Environment Variables**: Never commit .env files
4. **Database Security**: Use strong passwords and restrict network access
5. **Regular Updates**: Keep dependencies updated

### Configuration

```env
# Use strong secret keys
SECRET_KEY=<generate-with-openssl-rand-hex-32>

# Use strong database passwords
POSTGRES_PASSWORD=<strong-random-password>

# Disable debug in production
DEBUG=False
```

### Docker Security

- Run containers as non-root users
- Use specific image versions, not "latest"
- Scan images for vulnerabilities
- Limit container resources

## Known Issues

None at this time.
