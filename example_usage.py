from client import CreatorMsaContractDeliverableEscrowClient

def main():
    client = CreatorMsaContractDeliverableEscrowClient()
    res = client.escrow_campaign_deliverables('crt_tech_9918', 3500.00, ['1x TikTok Video', '1x Story with Link'])
    print('Creator MSA Contract Escrow: ' + res['contract_escrow_id'] + ' (Status: ' + res['contract_status'] + ')')
    print('Escrowed: $' + str(res['escrowed_amount_usd']) + ' | Milestones: ' + str(res['milestones_pending_verification_count']))
    print('Rights Clause: ' + str(res['automatic_rights_assignment_clause_included']))
    print('Escrow Dossier: ' + res['smart_contract_escrow_dossier_url'])

if __name__ == '__main__':
    main()
