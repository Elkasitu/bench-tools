def main(env):
    fields = env['ir.model.fields'].search([])
    fields.mapped('model_id.name')
